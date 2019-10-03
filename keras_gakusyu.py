from keras.datasets import mnist
from keras.models import load_model
from keras.utils import np_utils
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = np.array(X_train)/255
X_test = np.array(X_test)/255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

model = load_model("tegaki-number-vol2.hdf5")

hist = model.fit(X_train, y_train, batch_size=200, verbose=1,
                 epochs=10, validation_split=0.1)

score = model.evaluate(X_test, y_test, verbose=1)
print("正解率(acc)：", score[1])

model.save("tegaki-number-vol2.hdf5")