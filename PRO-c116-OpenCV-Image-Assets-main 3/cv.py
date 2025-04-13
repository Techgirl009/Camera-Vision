import cv2
#camera vison is the full form of cv, it is a module that without it, the computer can't see pictures
import numpy as np
#numpy stands for numerical python, using numpy mathematical and logical operations on arrays can be performed.
img = cv2.imread("butterfly.jpg")
#the computer is reading the image
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#turning the image into greyscale
#cv2.imshow("displayimage", gray_img)
#the image will be shown, once you show then only the image will show.
black = np.zeros([398, 398])
#cv2.waitKey(10000)
#the waitkey means that how long you want to see the picture.
print(black)
cv2.imshow("black", black)
cv2.waitKey(10000)