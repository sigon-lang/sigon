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
from sklearn import preprocessing, model_selection
import matplotlib.pyplot as plt


#import deep learning modules
from keras.models import Sequential, Model, load_model
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Input, UpSampling2D, Conv1D, GlobalMaxPooling1D, Embedding, Multiply, Dropout


from keras import optimizers, utils
from keras.callbacks import EarlyStopping
import multiprocessing
import os


class NNCtx(ContextService):

    _instance = None    
    histories_evaluate = [] # contains information about previous training
    histories_training = [] # contains information about previous training
    data_type = 'train' # test or predict    
    epochs = 15
    feature_extraction_epochs = 10
    model_name = "CNN_EMBER"
    feature_extraction_model = None
    mode = 'train' # NOTE I dont know if this is right
    delta = 1
    delta_rate = 0.0025
    model_parameters = {
            'patience': 5,
            'min_delta': 0
    }
    data_path = []
    
    
    
    
    
    @classmethod
    def __new__(cls, load_model=False, model_dir='./model'):
        if load_model:
            cls.model = load_model(model_dir)        
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        # set parameters config
        # cls.model_parameters = {
        #     'patience': 5,
        #     'min_delta': 0
        # }
        
        return cls._instance

    @classmethod
    def verify(self, fact): 
        # NOTE: can return info about history accuracy(2) - returns accuary on the second month
        if 'history_evaluations' in fact:
            return [{fact: self.histories_evaluate}]
        elif 'history_trainings' in fact:
            return [{fact: self.histories_training}]            
        
        return []
    @classmethod
    def fine_tuning(self, config):
        print('fine tuning model')
        self.feature_extraction(config)
        # self.histories.pop() # removing last history that should not be considered
        self.model.trainable = True

        
        self.model.summary()

        self.model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
        self.data_type = config.get('data_type', 'train')
        x_test0, y_test0 = self.load_data(config['path'])

        early_stopping = EarlyStopping(monitor='val_loss', min_delta=self.model_parameters['min_delta'] ,patience=self.model_parameters['patience'], verbose=1)        
        history = self.model.fit(x_test0, y_test0, validation_split=0.2, epochs=self.epochs, callbacks=[])

        print({
            'accuracy': history.history['accuracy'][-1],
            'loss': history.history['loss'][-1]
        })
        self.histories_training.append({
            'accuracy': history.history['accuracy'][-1],
            'loss': history.history['loss'][-1]
        })


        # loss, acc = self.model.evaluate(x_test0,y_test0)
        # print("loss: " + str(loss))
        # print("acc: " + str(acc))

        self.model.save(self.format_model_name(config['month'], 'fine_tuning'), overwrite=True)
    
    @classmethod
    def format_model_name(self, month, mode):
        return f'nn-models/{self.model_name}-{month}-{mode}.keras' 

    @classmethod
    def feature_extraction(self, config):
        print('feature extracting model')
        # I can set a config to check if a feature extraction is already available
        if 'model_dir' in config and config['model_dir'] != '':
            base_model= load_model(config['model_dir'])
        else:
            base_model = self.model.__copy__()
            
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
        self.data_type = config.get('data_type', 'train')
        x_test0, y_test0 = self.load_data(config['path'])

        # early_stopping = EarlyStopping(monitor='val_loss', min_delta=self.model_parameters['min_delta'] ,patience=self.model_parameters['patience'], verbose=1)        
        
        history = self.model.fit(x_test0, y_test0, validation_split=0.3, epochs=self.feature_extraction_epochs, callbacks=[])

        print({
            'accuracy': history.history['accuracy'][-1],
            'loss': history.history['loss'][-1]
        })

        self.histories_training.append({
            'accuracy': history.history['accuracy'][-1],
            'loss': history.history['loss'][-1]
        })

        self.model.save(self.format_model_name(config['month'], 'feature_extraction'), overwrite=True)


    
    @classmethod
    def test_model(self, config):
        if config['model_dir'] != '':
            model = load_model(config['model_dir'])        
        else:
            model = self.model
        self.data_type = config.get('data_type', 'test')
        x_test0, y_test0 = self.load_data(config['path'])        
        loss, acc = model.evaluate(x_test0,y_test0)
        # adequar para poder colocar no histories
        self.histories_evaluate.append({
            'accuracy': acc,
            'loss': loss
        })        
    
    @classmethod
    def train_model(self, config):
        print('training model')

        self.model = Sequential()

        INPUT_SHAPE = (48, 48, 1)

        self.model.add(Conv2D(filters=128, kernel_size=(3,3),  activation='relu', input_shape=INPUT_SHAPE))
        self.model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
        self.model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2), padding='valid'))
        self.model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu'))
        self.model.add(Flatten())

        self.model.add(Dense(400, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

        # view model layers
        self.model.summary()

        # compile model
        self.model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['accuracy'])
        self.data_type = config.get('data_type', 'train')
        x_train0, y_train0 = self.load_data(config['path'])

        early_stopping = EarlyStopping(monitor='val_loss', min_delta=self.model_parameters['min_delta'] ,patience=self.model_parameters['patience'], verbose=1)        


        # fit our model
        history = self.model.fit(x_train0, y_train0, validation_split=0.3, epochs=self.epochs, callbacks=[])
        # save the model
        self.model.save(self.format_model_name(config['month'], 'train'), overwrite=True)
        self.histories_training.append({
            'accuracy': history.history['accuracy'][-1],
            'loss': history.history['loss'][-1]
        })
        

    @classmethod
    def load_data(self, path):
        x_dat = 'X_' + self.data_type + '.dat'
        y_dat = 'y_' + self.data_type + '.dat'
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


    def predict(self, config):
        pass 

    @classmethod
    def create_config(self, fact):
        # parse path to get the month
        path = fact[fact.find("(")+1:fact.find(")")]
        month = path.split('/')[-1]
        return {
            'mode': self.mode,
            'month': month,
            'path': fact[fact.find("(")+1:fact.find(")")],
            'model_dir': ''
        }
    
    @classmethod
    def update_parameters(self, fact):
        
        patience_action = fact.get('patience', 'keep')
        # min_delta_action = fact.get('min_delta', 'keep')
        if patience_action == 'increase':
            self.model_parameters['patience'] = self.model_parameters['patience']+self.delta
            self.model_parameters['min_delta'] -= self.delta_rate 
            if self.model_parameters['min_delta'] < 0:
                self.model_parameters['min_delta'] = 0
            
            return
        elif patience_action == 'decrease':
            self.model_parameters['patience'] = self.model_parameters['patience']-self.delta
            self.model_parameters['min_delta'] += self.delta_rate
            if self.model_parameters['patience'] < 0:
                self.model_parameters['patience'] = 0
                return
        elif patience_action == 'increase2x':        
            self.model_parameters['patience'] += (2*self.delta)
        

        
        # self.model_parameters['min_delta'] = self.model_parameters['patience']+self.delta if patience_action == 'increase' else self.model_parameters['patience']-self.delta

        

    @classmethod
    def append_fact(self, fact) -> bool: # can train, test or predict
        # here fact only have a dir to the current data
        print(fact)
        try:
            if 'patience' in fact and 'min_delta' in fact:
                self.update_parameters(fact)
                return True

            if 'setOperation' in fact:
                print({
                    'setOperation': fact
                })
                self.mode = fact[fact.find("(")+1:fact.find(")")]            
                return True
            elif 'execute' in fact:
                config = self.create_config(fact)
                print({'config': config})
                operations = {
                    'test': self.test_model,
                    'train': self.train_model,
                    'fineTuning': self.fine_tuning,
                    'featureExtraction': self.feature_extraction,
                    'predict': self.predict
                }
                operations[config.get('mode', 'test')](config)
                # test the model after train, fine_tuning or FE
                # if config['mode'] != 'test' and config['mode'] != 'predict':
                #     self.test_model(config)
                
                self.mode = ''
                return True

            return False
            
        except Exception as e: 
            print('error while processing fact', e)

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



            



    
# TEST - OK
# fact = {
#         'month': '01',
#         'mode': 'train',        
#         'path': '/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01'
# }

# TEST - OK
# fact = {
#     'month': '01',
#     'mode': 'test',
#     'model_dir': 'CNN_EMBER-01-train.h5',
#     'path': '/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01'
# }

# TEST - OK
# fact = {
#         'mode': 'feature_extraction',
#         'month': '01',
#         'model_dir': 'CNN_EMBER-01-train.h5',
#         'path': '/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01'
# }

# fact = {
#         'mode': 'fine_tuning',
#         'month': '01',
#         'model_dir': 'CNN_EMBER-01-train.h5',
#         'path': '/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01'
# }

# # fact = {
# #         'mode': 'predict',
# #         'input': '',
# #         'data_dir': '/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01'
# # }

# NNCtx.ctx_name = '_nn'

# NNCtx.append_fact(fact)
# # OK
# # NNCtx.train_model(path='/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01') 

# NNCtx.data_type = 'train'

# NNCtx.feature_extraction(path='/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-02', model_dir='/home/rr/repositorios/experimento-final-tese/sigon/CNN_EMBER.h5')






# OK
# NNCtx.fine_tuning(path='/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-02', model_dir='/home/rr/repositorios/experimento-final-tese/sigon/CNN_EMBER.h5')


# NNCtx.data_type = 'test'

# NNCtx.test_model(path='/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-02') 
