# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
import argparse
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import time

#import deep learning modules
from keras.models import Sequential, Model, load_model
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Input, UpSampling2D, Conv1D, GlobalMaxPooling1D, Embedding, Multiply



from keras import optimizers, utils
from keras.callbacks import EarlyStopping
import multiprocessing
import os

utils.set_random_seed(812)

parser = argparse.ArgumentParser('./main.py', description='Run individual continual learning experiment.')
parser.add_argument('--data-dir', type=str, default='./datasets', dest='d_dir', help="default: %(default)s")
parser.add_argument('--results-dir', type=str, default='./results', dest='r_dir', help="default: %(default)s")
parser.add_argument('--model-name', type=str, default='./models', dest='model_name', help="default: %(default)s")
parser.add_argument('--epochs', type=str, default='2', dest='epochs', help="default epochs: %(default)s")




def run(args):

    # path = "/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01/"
    path = args.d_dir
    print (path)

    

    x_train = np.memmap(os.path.join(path, 'X_train.dat'), mode="r+", dtype=np.float32)
    y_train = np.memmap(os.path.join(path, 'y_train.dat'), mode="r+", dtype=np.float32)


    y_train = np.memmap(os.path.join(path, 'y_train.dat'), dtype=np.float32, mode="r")
    N = y_train.shape[0]
    x_train = np.memmap(os.path.join(path, 'X_train.dat'), dtype=np.float32, mode="r+", shape=(N, 2381))


    #make into a dataframe
    x_train = pd.DataFrame(x_train)
    y_train = pd.DataFrame(y_train)
    print(x_train.shape)
    print(y_train.shape)


    # Combining features and lables of train dataset
    x_train[2381] = y_train[0]
    x_train.shape, y_train.shape

    #remove unlabelled rows from the dataframe
    x_train.drop(x_train[(x_train[2381] == -1)].index, inplace=True)
    y_train.drop(y_train[(y_train[0] == -1)].index, inplace=True)
    print(x_train.shape)
    print(y_train.shape)

    #reconstructing the X_train dataframe
    x_train.drop([2381], axis =1, inplace=True)
    x_train.shape, y_train.shape

    x_train0 = x_train.values
    y_train0 = y_train.values

    # dimension reduction
    print(x_train0.shape)
    x_train0 = np.delete(x_train0, np.s_[-77:], axis=1)
    print(x_train0.shape)

    # normalize data for printing (pixels range: [0, 255])
    min_max_scaler = preprocessing.MinMaxScaler((0, 255), copy=False)
    x_train0 = min_max_scaler.fit_transform(x_train0)


    # reshape the data to consider vectors as images
    x_train0 = np.reshape(x_train0, (len(x_train0), 48, 48))


    x_train0 = x_train0 / 255.0

    # reshpe for CNN
    x_train0 = np.reshape(x_train0, (len(x_train0), 48, 48, 1))


    #define input shape
    INPUT_SHAPE = (48, 48, 1)

    embedding_size = 8 

    # define model structure
    # inp = Input( shape=(maxlen,))
    # emb = Embedding( INPUT_SHAPE, embedding_size )( inp )
    # filt = Conv1D( filters=128, kernel_size=500, strides=500, use_bias=True, activation='relu', padding='valid' )
    # attn = Conv1D( filters=128, kernel_size=500, strides=500, use_bias=True, activation='sigmoid', padding='valid')
    # gated = Multiply()([filt,attn])
    # feat = GlobalMaxPooling1D()( gated )
    # dense = Dense(128, activation='relu')(feat)
    # outp = Dense(1, activation='sigmoid')(dense)

    # basemodel = Model( inp, outp )

    model = Sequential()

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

    early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1, restore_best_weights=True)


    # fit our model
    history = model.fit(x_train0, y_train0, validation_split=0.2, epochs=args.epochs, callbacks=[early_stopping])
    # save the model
    model.save(args.model_name)

    

    


if __name__ == '__main__':
    # -load input-arguments
    args = parser.parse_args()
    args = argparse.Namespace(epochs=50, d_dir='/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01', model_name="model2018-01-b.h5")
    # -set default-values for certain arguments based on chosen scenario & experiment
    # -run experiment
    run(args)