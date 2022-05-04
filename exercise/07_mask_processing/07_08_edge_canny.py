import numpy as np, cv2

image = cv2.imread("../../resources/images07/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

canny = cv2.Canny(image, 100, 150)

cv2.imshow("image", image)
cv2.imshow("Canny", canny)
cv2.waitKey(0)