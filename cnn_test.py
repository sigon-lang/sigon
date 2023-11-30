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
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Input, UpSampling2D

from keras import optimizers
from keras.callbacks import EarlyStopping
import multiprocessing
import os



parser = argparse.ArgumentParser('./main.py', description='Run individual continual learning experiment.')
parser.add_argument('--data-dir', type=str, default='./datasets', dest='d_dir', help="default: %(default)s")
parser.add_argument('--x_test', type=str, default='X_test.dat', dest='x_test', help="default: %(default)s")
parser.add_argument('--y_test', type=str, default='y_test.dat', dest='y_test', help="default: %(default)s")



parser.add_argument('--results-dir', type=str, default='./results', dest='r_dir', help="default: %(default)s")
parser.add_argument('--model-name', type=str, default='./models', dest='model_name', help="default: %(default)s")
parser.add_argument('--epochs', type=str, default='2', dest='epochs', help="default epochs: %(default)s")

def run(args):

    path = args.d_dir
    print (path)

    x_test = np.memmap(os.path.join(path, args.x_test), mode="r+", dtype=np.float32)
    y_test = np.memmap(os.path.join(path, args.y_test), mode="r+", dtype=np.float32)


    y_test = np.memmap(os.path.join(path, args.y_test), dtype=np.float32, mode="r")
    N = y_test.shape[0]
    x_test = np.memmap(os.path.join(path, args.x_test), dtype=np.float32, mode="r+", shape=(N, 2381))


    #make into a dataframe
    x_test = pd.DataFrame(x_test)
    y_test = pd.DataFrame(y_test)
    print(x_test.shape)
    print(y_test.shape)


    # Combining features and lables of train dataset
    x_test[2381] = y_test[0]
    x_test.shape, y_test.shape

    #remove unlabelled rows from the dataframe
    x_test.drop(x_test[(x_test[2381] == -1)].index, inplace=True)
    y_test.drop(y_test[(y_test[0] == -1)].index, inplace=True)
    print(x_test.shape)
    print(y_test.shape)

    #reconstructing the X_train dataframe
    x_test.drop([2381], axis =1, inplace=True)
    x_test.shape, y_test.shape

    x_test0 = x_test.values
    y_test0 = y_test.values

    # dimension reduction
    print(x_test0.shape)
    x_test0 = np.delete(x_test0, np.s_[-77:], axis=1)
    print(x_test0.shape)

    # normalize data for printing (pixels range: [0, 255])
    min_max_scaler = preprocessing.MinMaxScaler((0, 255), copy=False)
    x_test0 = min_max_scaler.fit_transform(x_test0)


    # reshape the data to consider vectors as images
    x_test0 = np.reshape(x_test0, (len(x_test0), 48, 48))


    x_test0 = x_test0 / 255.0

    # reshpe for CNN
    x_test0 = np.reshape(x_test0, (len(x_test0), 48, 48, 1))

    model= load_model(args.model_name)


    loss, acc = model.evaluate(x_test0,y_test0)
    print("loss: " + str(loss))
    print("acc: " + str(acc))


if __name__ == '__main__':
    # -load input-arguments
    args = parser.parse_args()
    args = argparse.Namespace(x_test="X_train.dat", y_test= "y_train.dat",d_dir='/home/rr/repositorios/experimento-final-tese/continual-learning-malware/ember2018/month_based_processing_with_family_labels/2018-01', model_name="cnn-finetuning18-01.h5")
    # -set default-values for certain arguments based on chosen scenario & experiment
    # -run experiment
    run(args)
