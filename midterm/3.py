# 트랙바를 이용하여 이미지 블렌딩(blending)
import numpy as np, cv2

# image1의 가중치인 alpha값 변경해주는 콜백함수
def onChangeAlpha(value):
    global alpha, beta
    alpha = value / 100
    blendingImage = cv2.addWeighted(image1, alpha, image2, beta, 0)
    # 결과값만 출력
    dst[0:300, 300:600] = blendingImage
    cv2.imshow(title, dst)
# image2의 가중치인 beta값 변경해주는 콜백함수
def onChangeBeta(value):
    global alpha, beta
    beta = value / 100
    blendingImage = cv2.addWeighted(image1, alpha, image2, beta, 0)
    dst[0:300, 300:600] = blendingImage
    cv2.imshow(title, dst)


global dst, image1, image2, blendingImage
image1 = cv2.imread('images/add1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('images/add2.jpg', cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상파일 읽기 오류")

default = 50
alpha = default / 100; beta = default / 100
blendingImage = image = np.zeros((300, 300), np.uint8)

dst = np.zeros((300, image1.shape[0] + image2.shape[0] + 300), np.uint8)
dst[0:300, 0:300] = image1
dst[0:300, 600:900] = image2
title = 'dst'

cv2.imshow(title, dst)
cv2.createTrackbar('image1', title, default, 100, onChangeAlpha)
cv2.createTrackbar('image2', title, default, 100, onChangeBeta)

cv2.waitKey(0)
cv2.destroyAllWindows()