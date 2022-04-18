import tensorflow as tf
from tensorflow.keras.datasets import cifar10
import tensorflow.keras as keras
import numpy as np
from keras import models
from keras import layers
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import *
from tensorflow.keras import utils
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import img_to_array
from sklearn.model_selection import train_test_split


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

y_train = utils.to_categorical(y_train)
y_test = utils.to_categorical(y_test)

x_train = np.reshape(x_train, (-1,32,32,3))
x_test = np.reshape(x_test, (-1,32,32,3))

x_train = tf.image.resize_with_pad(x_train, 80, 80)

train_X = np.asarray([img_to_array(im) for im in x_train])

x_train, x_val, y_train, y_val = train_test_split(train_X,
                                  y_train,
                                  test_size=0.2,
                                  random_state=13
)

train_generator = ImageDataGenerator(
      rescale=1./255,
      rotation_range=20,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest'
)

test_generator = ImageDataGenerator(
    rescale=1./255
)

train_generator.fit(x_train)
test_generator.fit(x_val)

train_generator = train_generator.flow(x_train,y_train,batch_size=200)
test_generator = test_generator.flow(x_val,y_val,batch_size=200)

conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(80, 80, 3))
conv_base.trainable = False

model = models.Sequential([
   conv_base,
   layers.Flatten(),
   layers.Dropout(0.3),
   layers.Dense(256, activation="relu"),
   layers.Dense(128, activation="relu"),
   layers.Dense(10, activation="softmax"),
])

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.RMSprop(1e-4),
              metrics=['acc'])

history = model.fit(train_generator,
                    epochs=20,
                    # steps_per_epoch=1000,
                    batch_size=32,
                    validation_data=test_generator,
                    validation_steps=50,
                    shuffle=True,
                    )

conv_base.trainable = True

set_trainable = False
for layer in conv_base.layers:
    if layer.name == 'block3_conv1':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

model = models.Sequential([
   conv_base,
   layers.Flatten(),
   layers.Dropout(0.3),
   layers.Dense(256, activation="relu"),
   layers.Dense(128, activation="relu"),
   layers.Dense(10, activation="softmax"),
])

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.RMSprop(1e-4),
              metrics=['acc'])

history = model.fit(train_generator,
                    epochs=20,
                    # steps_per_epoch=1000,
                    batch_size=32,
                    validation_data=test_generator,
                    validation_steps=50,
                    shuffle=True,
                    )

model.save("vgg16_cifar10_new.hdf5")

