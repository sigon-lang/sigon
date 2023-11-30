from mcs.contexts.ctx_service import ContextService

import numpy as np
import pandas as pd
import pickle
import json
import math
import decimal
import time

import numpy as np 
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt


#import deep learning modules
from keras.models import Sequential, Model, load_model
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Input, UpSampling2D, Conv1D, GlobalMaxPooling1D, Embedding, Multiply, Dropout


from keras import optimizers
from keras.callbacks import EarlyStopping
import multiprocessing
import os

class NNCtx(ContextService):

    _instance = None    
    histories = [] # contains information about previous training
    mode = 'train' # test or predict    
    epochs = 5
    feature_extraction_epochs = 10
    model_name = "CNN_EMBER.h5"
    
    
    
    
    
    @classmethod
    def __new__(cls, load_model=False, model_dir='./model'):
        if load_model:
            cls.model = load_model(model_dir)        
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance

    @classmethod
    def verify(self, fact): 
        # NOTE: can return info about history accuracy(2) - returns accuary on the second month
        return []
    
    def fine_tuning(self, path, model_dir):
        new_model = self.feature_extraction(path, model_dir)
        self.histories.pop() # removing last history that should not be considered
        new_model.trainable = True
        self.model.summary()

        self.model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

        x_test0, y_test0 = self.load_data(path)
        history = self.model.fit(x_test0, y_test0, validation_split=0.3, epochs=self.epochs)


        self.histories.append(history)


        loss, acc = self.model.evaluate(x_test0,y_test0)
        print("loss: " + str(loss))
        print("acc: " + str(acc))

        self.model.save(self.model_name, overwrite=True)
    
    def feature_extraction(self, path, model_dir):

        base_model= load_model(model_dir)
        base_model.trainable = False

        # Create new model on top
        inputs = Input(shape=(48, 48, 1))        
        
        outputs = base_model.layers[-2].output         
        new_model = Model(inputs=base_model.inputs, outputs=outputs)
        
        x = new_model(inputs, training=False)
        x = Dropout(0.3)(x)  # Regularize with dropout
        outputs = Dense(1, activation='sigmoid')(x)
        self.model = Model(inputs, outputs)

        self.model.summary()
        self.model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

        x_test0, y_test0 = self.load_data(path)
        
        history = self.model.fit(x_test0, y_test0, validation_split=0.3, epochs=self.feature_extraction_epochs)

        self.histories.append(history)

        return new_model

    

    def test_model(self, path, model_dir):
        model = load_model(model_dir)
        x_test0, y_test0 = self.load_data(path)
        loss, acc = model.evaluate(x_test0,y_test0)
        return loss, acc
    

    def train_model(self, path):

        model = Sequential()

        INPUT_SHAPE = (48, 48, 1)

        model.add(Conv2D(filters=128, kernel_size=(3,3),  activation='relu', input_shape=INPUT_SHAPE))
        model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
        model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
        model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu'))
        model.add(Flatten())

        model.add(Dense(400, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        # view model layers
        model.summary()

        # compile model
        model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])

        x_train0, y_train0 = self.load_data(path)

        # fit our model
        history = model.fit(x_train0, y_train0, validation_split=0.2, epochs=self.epochs)
        # save the model
        model.save(self.model_name)

        self.histories.append(history)


    def load_data(self, path):
        x_dat = 'X' + self.mode + '.dat'
        y_dat = 'y' + self.mode + '.dat'
        x_train = np.memmap(os.path.join(path, x_dat), mode="r+", dtype=np.float32)
        y_train = np.memmap(os.path.join(path, y_dat), mode="r+", dtype=np.float32)


        y_train = np.memmap(os.path.join(path, y_dat), dtype=np.float32, mode="r")
        N = y_train.shape[0]
        x_train = np.memmap(os.path.join(path, x_dat), dtype=np.float32, mode="r+", shape=(N, 2381))


        #make into a dataframe
        x_train = pd.DataFrame(x_train)
        y_train = pd.DataFrame(y_train)

        # Combining features and lables of train dataset
        x_train[2381] = y_train[0]
        x_train.shape, y_train.shape

        #remove unlabelled rows from the dataframe
        x_train.drop(x_train[(x_train[2381] == -1)].index, inplace=True)
        y_train.drop(y_train[(y_train[0] == -1)].index, inplace=True)        

        #reconstructing the X_train dataframe
        x_train.drop([2381], axis =1, inplace=True)
        x_train.shape, y_train.shape

        x_train0 = x_train.values
        y_train0 = y_train.values

        # dimension reduction
        
        x_train0 = np.delete(x_train0, np.s_[-77:], axis=1)
        

        # normalize data for printing (pixels range: [0, 255])
        min_max_scaler = preprocessing.MinMaxScaler((0, 255), copy=False)
        x_train0 = min_max_scaler.fit_transform(x_train0)


        # reshape the data to consider vectors as images
        x_train0 = np.reshape(x_train0, (len(x_train0), 48, 48))


        x_train0 = x_train0 / 255.0

        # reshpe for CNN
        x_train0 = np.reshape(x_train0, (len(x_train0), 48, 48, 1))

        return x_train0, y_train0

        

    @classmethod
    def append_fact(self, fact) -> bool: # can train, test or predict
        # here fact only have a dir to the current data
        #start_time = time.time()        
        fact = json.loads(fact)
        self.check_keys(fact)
        self.data.update(fact)  
        entry = pd.DataFrame([self.data])
        encoded_entry = self.enc.transform(entry).toarray()

        entry_torch = torch.tensor(np.array(encoded_entry), dtype=torch.float)
        formated_entry = torch.tensor(np.array(entry_torch), dtype = torch.float)
        self.avg_salary = (self.model.forward(formated_entry).item()*1000)/12
        #print("tempo da nn {}".format(time.time() - start_time))
        
        return True

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True

    @classmethod
    def check_keys(self, fact):
        keys_to_remove = []
        for key in fact.keys():
            if key not in self.data:
                keys_to_remove.append(key)
                
        for key in keys_to_remove:
            del fact[key]                


    @classmethod
    def reset(cls):
        cls._instance = None