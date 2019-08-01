import keras
from keras.datasets import mnist
from matplotlib import pyplot

(X_train,y_train),(X_test,y_test)=mnist.load_data()

for i in range(0,32):
    pyplot.subplot(4,8,i+1)
    pyplot,imshow(X_train[i],cmap='gray')

pyplot.show()