import cv2

image = cv2.imread("../../resources/images6/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

# OpenCV 함수 이용(saturation 방식)
dst1 = cv2.add(image, 100)
dst2 = cv2.subtract(image, 100)

# numpy/ndarray 이용(modulo 방식)
dst3 = image + 100
dst4 = image - 100

cv2.imshow("original image", image)
cv2.imshow("dst1-bright:OpenCV", dst1)
cv2.imshow("dst2-dark:OpenCV", dst2)
cv2.imshow("dst3-bright:numpy", dst3)
cv2.imshow("dst4-bright:numpy", dst4)
cv2.waitKey(0)