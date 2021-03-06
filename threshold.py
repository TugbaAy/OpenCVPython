# -*- coding: utf-8 -*-

import cv2

img1 = cv2.imread("D:/bulmaca.png")
cv2.imshow("Bulmaca",img1)

img2 = cv2.imread("D:/gazete.jpeg")
cv2.imshow("Gazete",img2)
gray_image = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# ilk resmi ikincinin boyutuna getiriyoruz, aksi takdirde hata alırız.

img1_resized = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

#iki resmi birbirine ekliyoruz. 

"""
parametreleri
    ilk resim
    ilk resmin ağırlığı
    ikinci resim
    ikinci resmin ağırlığı
    ..
"""

dst = cv2.addWeighted(img2,0.7,img1_resized,0.3,0)

cv2.imshow("a",dst)


ret, threshold = cv2.threshold(gray_image,170,255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshold",threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()