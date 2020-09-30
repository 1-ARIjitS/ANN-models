# -*- coding: utf-8 -*-
"""ANN MNIST .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKLukhHa0mOTG2BBrKnlJawBK1ZYaEC0
"""

import keras

from keras.datasets import mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()

x_train=x_train.reshape(60000,784)
x_test=x_test.reshape(10000,784)

x_train=x_train.astype('float32')
x_test=x_test.astype('float32')
x_train/=255
x_test/=255

from keras.utils import np_utils

y_train=np_utils.to_categorical(y_train,10)
y_test=np_utils.to_categorical(y_test,10)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers.core import Dense, Dropout, Activation

model=Sequential(Dropout(0.2))
model.add(Dense(512, activation='relu', input_dim=784))
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy' ,
    metrics=['accuracy']
    
)

model.fit(x_train,y_train,batch_size=128,epochs=10)

model.evaluate(x_train,y_train)