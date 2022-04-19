import numpy as np
import tensorflow as tf
from os.path import exists
from PIL import Image
import gdown

if not exists("vgg16_cifar10_new.hdf5"):
    url = 'https://drive.google.com/file/d/1LJnhd4X4GIjoaBv40DtgxGryT33xQykT/view?usp=sharing'
    output = 'vgg16_cifar10_new.hdf5'
    gdown.download(url, output, quiet=False, fuzzy=True)

model_filename = "vgg16_cifar10_new.hdf5"
model = tf.keras.models.load_model(model_filename)


LABEL_NAMES = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']


def resize_image(image_to_recognize):
    img = Image.open(image_to_recognize)
    img = img.resize((80, 80))
    img = img.convert("RGB")
    input_image = np.reshape(img, (-1, 80, 80, 3))
    return input_image


def predict_image(image):
    input_img = resize_image(image)
    predict_img = model.predict(input_img)
    pred_class = LABEL_NAMES[np.argmax(predict_img)]
    return pred_class

