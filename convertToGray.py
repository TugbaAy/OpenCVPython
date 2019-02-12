# -*- coding: utf-8 -*-
import cv2


imgLena = cv2.imread("D:/Lena.jpg")
gray_image = cv2.cvtColor(imgLena,cv2.COLOR_BGR2GRAY)
cv2.imshow("Lena Gray",gray_image)

col, rows, ch = imgLena.shape

print(col)
print(rows)
print(ch)

kesik = imgLena[10:rows,10:col]
cv2.imshow("Kesik" , kesik)

cv2.waitKey(0)
cv2.destroyAllWindows()