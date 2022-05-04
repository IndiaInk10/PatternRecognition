import numpy as np, cv2

image = cv2.imread("../../resources/images07/filter_sharpen.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1= [0, -1, 0,
        -1, 5, -1,
        ]