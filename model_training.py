from tensorflow.keras.models import Sequential
from keras import optimizers
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


train_dir = 'icons/train'
validation_dir = 'icons/validation'
test_dir = 'icons/test'

# small CNN
model = Sequential([
Conv2D(32, (3, 3), activation='relu', input_shape=(400, 400, 3)),
MaxPooling2D((2, 2)),
Conv2D(64, (3, 3), activation='relu'),
MaxPooling2D((2, 2)),
Conv2D(128, (3, 3), activation='relu'),
MaxPooling2D((2, 2)),
Conv2D(256, (3, 3), activation='relu'),
MaxPooling2D((2, 2)),
Conv2D(256, (3, 3), activation='relu'),
MaxPooling2D((2, 2)),
Conv2D(128, (3, 3), activation='relu'),
Flatten(),
Dropout(0.5),
Dense(512, activation='relu'),
Dense(57, activation='softmax')
])

print(model.summary())

# compile model
model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=1e-4), metrics=['acc'])

# read images from directory
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=40, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.1, zoom_range=0.1, horizontal_flip=True, vertical_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)