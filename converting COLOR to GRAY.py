#converting colour image to greyscale image

import cv2
image = cv2.imread('sample1.png')
greyImage = cv2.cvtcolor(image.cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png',greyImage)
cv2.imshow('color_image',image)
cv2.imshow('Grey_image',greyImage)
cv2.waitkey(0)
cv2.destroyAllWindows()
