# -*- coding: utf-8 -*-

import cv2

araba = cv2.imread("D:/car.jpeg")
cv2.imshow("Araba",araba)

yol = cv2.imread("D:/road.jpeg")
cv2.imshow("Yol",yol)

gray_image = cv2.cvtColor(yol,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(gray_image,100,10,cv2.THRESH_BINARY)
araba_boyutlandirilmis = cv2.resize(araba, (yol.shape[1], yol.shape[0]))


yolVeAraba = cv2.add(araba_boyutlandirilmis, yol, mask = mask)
cv2.imshow("Birlestirilmis Yol ve Araba",yolVeAraba)

cv2.waitKey(0)
cv2.destroyAllWindows()