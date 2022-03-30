import cv2
import numpy as np

image = cv2.imread("../../resources/images_5/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")
if image.ndim != 3: raise Exception("컬러 영상 아님")

bgr = cv2.split(image)
# BGR
print("bgr 자료형:", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소개수:", len(bgr))

# 각 채널을 윈도우에 띄우기
cv2.imshow("image", image)
onlyBlue = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)
for h in range(0, onlyBlue.shape[0]):
    for w in range(0, onlyBlue.shape[1]):
        onlyBlue[h][w][0] = bgr[0][h][w]
# 행렬의 특정 부분의 차를 구하는 방법을 찾아보자
cv2.imshow("Only Blue", onlyBlue)
cv2.imshow("Remove Blue", image - onlyBlue)
cv2.imshow("Blue Channel", bgr[0])
cv2.imshow("Green Channel", bgr[1])
cv2.imshow("Red Channel", bgr[2])

# cv2.imshow("Blue channel", image[:,:,0])
# cv2.imshow("Green channel", image[:,:,1])
# cv2.imshow("Red channel", image[:,:,2])
cv2.waitKey(0)