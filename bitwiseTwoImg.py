# -*- coding: utf-8 -*-
import cv2

print(cv2.__version__)

img1 = cv2.imread("D:/first.png")
cv2.imshow("First",img1)

img2 = cv2.imread("D:/second.png")
cv2.imshow("Second",img2)

bit_and = cv2.bitwise_and(img1,img2)
cv2.imshow("and",bit_and)

bit_or = cv2.bitwise_or(img1,img2)
cv2.imshow("or",bit_or)

cv2.waitKey(0)
cv2.destroyAllWindows()