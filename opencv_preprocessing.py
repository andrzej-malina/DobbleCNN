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
    plt.imshow(image, cmap='gray')
    plt.show()

def save_image(directory, image, name):
    path = join(directory, '{0}'.format(name)+'.jpg')
    cv2.imwrite(path, image)

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

def thresh_image(image, threshold=185):
    return cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]

def grab_contours_and_sort_by_area(image, threshold=185, all=False):
    image_grayed = gray_image(image)
    image_threshed = thresh_image(image_grayed, threshold=threshold)

    if all:
        contours = cv2.findContours(image_threshed.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours = cv2.findContours(image_threshed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)

    return sorted(contours, key=cv2.contourArea, reverse=True)

def draw_contour(image, contour):
    contour_image = cv2.drawContours(image, contour, -1, (255, 0, 0), 3)

    return contour_image

def add_images(image1, image2, hor=True):
    if hor:
        img = np.concatenate((image1, image2), axis=1)
    else:
        img = np.concatenate((image1, image2), axis=0)
    return img

#card in the foregroung
def keep_contour(image, cnt):
    gray = gray_image(image)
    mask = np.zeros(gray.shape, np.uint8)
    mask = cv2.drawContours(mask, [cnt], -1, 255, cv2.FILLED)
    output = image.copy()
    return cv2.bitwise_and(output, output, mask=mask)

# white background (use inverted mask)
def keep_contour_with_white_background(image, cnt):
    gray = gray_image(image)
    mask = np.zeros(gray.shape, np.uint8)
    mask = cv2.drawContours(mask, [cnt], -1, 255, cv2.FILLED)
    bk = np.full(image.shape, 255, dtype=np.uint8)
    fg_masked = cv2.bitwise_and(image, image, mask=mask)
    mask = cv2.bitwise_not(mask)
    bk_masked = cv2.bitwise_and(bk, bk, mask=mask)
    mask = cv2.bitwise_not(mask)
    return cv2.bitwise_or(fg_masked, bk_masked)

def get_rect_coordinates_around_contour(cnt):
    x,y,w,h = cv2.boundingRect(cnt)
    return x,y,w,h

def bounding_square_around_contour(cnt):
    x,y,w,h = get_rect_coordinates_around_contour(cnt)
    # create squares instead of rectangulars
    if w < h:
        x += int((w-h)/2)
        w = h
    else:
        y += int((h-w)/2)
        h = w
    return x, y, w, h

def take_out_icons(image, x, y, w, h):
    return image[y:y+h, x:x+w]

