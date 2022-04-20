# R, G, B 채널 별 밝기 표현하기
import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")
if image.ndim != 3: raise Exception("컬러 영상 아님")

bgr = cv2.split(image)

# 각 색상 채널을 저장할 행렬 생성
B = np.zeros((image.shape[0], image.shape[1], 3), image.dtype)
G = np.zeros((image.shape[0], image.shape[1], 3), image.dtype)
R = np.zeros((image.shape[0], image.shape[1], 3), image.dtype)

for h in range(0, image.shape[0]):
    for w in range(0, image.shape[1]):
        # 각 색상 채널에 맞게 한 색상 채널만 채우기
        B[h][w][0] = bgr[0][h][w]
        G[h][w][1] = bgr[1][h][w]
        R[h][w][2] = bgr[2][h][w]

cv2.imshow("Blue channel", B)
cv2.imshow("Green channel", G)
cv2.imshow("Red channel", R)

cv2.waitKey(0)