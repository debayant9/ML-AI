# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:05:27 2021

@author: Debayan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13]
y = dataset.iloc[:, 13]

geography = pd.get_dummies(X['Geography'], drop_first=True)
gender = pd.get_dummies(X.Gender, drop_first=True)

X = pd.concat([X, geography, gender], axis=1)

X = X.drop(['Geography', 'Gender'], axis=1)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Create the ANN

#Import Keras
import keras
from keras.models import Sequential
from keras.layers import Dense,LeakyReLU,PReLU,ELU,Dropout

# Initialize ANN
# Sequential groups a linear stack of layers into a tf.keras.Model.The input layer
# is auto created with size of (batch_size, input_dim)
classifier = Sequential() 
# Dense implements the operation out = activation(dot(input,kernel) + bias)
classifier.add(Dense(units = 6, kernel_initializer='he_uniform', activation='relu'))

# Adding the second hidden layer
classifier.add(Dense(units = 6, init = 'he_uniform',activation='relu'))
# Adding the output layer
classifier.add(Dense(units = 1, init = 'glorot_uniform', activation = 'sigmoid'))

classifier.compile(optimizer = 'Adamax', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
model_history=classifier.fit(X_train, y_train.values, validation_split=0.33, batch_size = 10, nb_epoch = 100)


print(model_history.history.keys())
# summarize history for accuracy
plt.plot(model_history.history['acc'])
plt.plot(model_history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


