import matplotlib.pyplot as plt
import numpy as np
import imutils
import cv2
from os.path import join

#function to add contrast to the image, returns image with better contrast
def add_contrast(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a,b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

imgname = 'test.jpg'

def read_image(image):
    return cv2.imread(image)

def display_image(image):
    plt.imshow(image)
    plt.show()

def resize_image(image, size=(800,800)):
    return cv2.resize(image, size)

def blur_image(image):
    return cv2.GaussianBlur(image, (11, 11), 0)

def combine(image, contrast=True, resize=True, blur=False):
    if contrast:
        img = add_contrast(image)
    if resize:
        img = resize_image(img)
    if blur:
        img = blur_image(img)

    return img

def gray_image(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def convert_color(image, toRGB=True):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def thresh_image(image, threshold=175):
    return cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]



