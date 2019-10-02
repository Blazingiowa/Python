import keras
from keras.datasets import mnist
from matplotlib import pyplot

(X_train,y_train),(X_test,y_test)=mnist.load_data()

for i in range(0,32):
    pyplot.subplot(4,8,i+1)
    pyplot.imshow(X_train[i],cmap='gray')

X_train=X_train.reshape(-1,784).astype('float32')/255
X_test=X_test.reshape(-1,784).astype('float32')/255

print(X_train)

y_train=keras.utils.np_utils.to_categorical(y_train.astype('int32'),10)
y_test=keras.utils.np_utils.to_categorical(y_train.astype('int32'),10)

in_size=28*28

out_size=10

Dense=keras.layers.Dense
model=keras.models.Sequential()
model.add(Dense(512,activation='relu',input_shape=(in_size,)))
model.add(Dense(out_size,activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

model.fit(X_train,y_train,batch_size=20,epochs=20)

score=model.evaluate(X_test,y_test,verbose=1)
print('正解率=',score[1],'loss=',score[0])
