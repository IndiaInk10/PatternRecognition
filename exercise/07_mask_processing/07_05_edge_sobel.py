import numpy as np, cv2

image = cv2.imread("../../resources/images07/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 1,
         -2, 0, 2,
         -1, 0, 1]
data2 = [-1, -2, -1,
         0, 0, 0,
         1, 2, 1]

dst1 = cv2.Sobel(image, cv2.CV_8U, 1, 0, 3)
dst2 = cv2.Sobel(image, cv2.CV_8U, 0, 1, 3)

cv2.imshow("dst1 - vertical", dst1)
cv2.imshow("dst2 - horizontal", dst2)
cv2.waitKey(0)