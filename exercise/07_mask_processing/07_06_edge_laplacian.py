import numpy as np, cv2

image = cv2.imread("../../resources/images07/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

dst = cv2.Laplacian(image, cv2.CV_8U, 1)

cv2.imshow("image", image)
cv2.imshow("Laplacian", dst)
cv2.waitKey(0)