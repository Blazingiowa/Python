import cv2
from sklearn.externals import joblib
import keras
from keras.models import load_model
from keras.utils.np_utils import to_categorical


def predict_digit(filename):
    model = load_model('tegaki-number.hdf5')
    model.load_weights('tegaki-number.hdf5')

    my_img = cv2.imread(filename)

    my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)

    my_img = cv2.resize(my_img, (8, 8))

    my_img = 15 - my_img // 16

    my_img = my_img.reshape((-1, 64))
    res = model.predict(my_img)
    return res[0]


n = predict_digit("four.png")
print("four.png = " + str(n))
n = predict_digit("five.png")
print("five.png = " + str(n))
