# 사각형 그리기
import numpy as np, cv2
import draw_histogram as dh

# 사각형 만들고 이미지 crop하는 마우스 콜백 함수
def onMouse(event, x, y, flags, param):
    global image, title, lCount, coord
    if event == cv2.EVENT_LBUTTONDOWN:
        if lCount == 0: coord = []
        coord.append([x, y])

        lCount += 1
        # 짝수번 클릭시
        if lCount == 2:
            tempImage = image.copy()
            cv2.rectangle(tempImage, coord[0], coord[1], (0, 0, 0), 2) # black, lineWidth = 2
            cv2.imshow(title, tempImage)

            # 사각형 반대로 좌표를 찍는 경우
            if coord[1][1] < coord[0][1]:
                coord[1][1], coord[0][1] = coord[0][1], coord[1][1]
            if coord[1][0] < coord[0][0]:
                coord[1][0], coord[0][0] = coord[0][0], coord[1][0]

            cropImage = image[coord[0][1]:coord[1][1], coord[0][0]:coord[1][0]].copy()
            cv2.imshow('crop_image', cropImage)

            # 계급하고 범위 설정
            bsize, ranges = [32], [0, 256]
            hist = cv2.calcHist([cropImage], [0], None, bsize, ranges)
            cv2.imshow('hist_img', dh.draw_histo(hist))
            lCount = 0


coord = []
lCount = 0

image = cv2.imread('images/pixel.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

title = 'result'
cv2.imshow(title, image)
while True:
    cv2.setMouseCallback(title, onMouse)
    cv2.waitKey(0)