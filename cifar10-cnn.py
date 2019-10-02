import matplotlib.pyplot as plt
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D,MaxPooling2D

num_classes=10
im_rows=32
im_cols=32
in_shape=(im_rows,im_cols,3)

(X_train,y_train),(X_test,y_test)=cifar10.load_data()

X_train=X_train.astype('float32')/255
X_test=X_test.astype('float32')/255

y_train=keras.utils.to_categorical(y_train,num_classes)
y_test=keras.utils.to_categorical(y_test,num_classes)

