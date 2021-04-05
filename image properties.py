#checking image properties

import cv2
img = cv2.imread('sample1.png')
print(img.shape)#(342,548,3)
print(img.size)#562248
print(img.dtype)#unit8
