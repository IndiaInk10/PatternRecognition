import numpy as np, cv2

image = cv2.imread("../../resources/images07/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 1,
         -2, 0, 2,
         -1, 0, 1]
data2 = [-1, -2, -1,
         0, 0, 0,
         1, 2, 1]