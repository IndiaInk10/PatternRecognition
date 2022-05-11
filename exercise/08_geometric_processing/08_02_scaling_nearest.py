import numpy as np, cv2
from header_area_08 import scaling


def scaling_nearst(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    print("i", i)
    print("j", j)
    y, x = np.int32(i/ratioY), np.int32(j/ratioX)
    print("x", x)
    print("y", y)
    # 행렬의 있는 값들을 index로 사용하여 한꺼번에 대입(?)
    dst[i,j] = img[y,x]

    return dst

image = cv2.imread("../../resources/images8/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dst1 = scaling(image, (350, 400))
dst2 = scaling_nearst(image, (350, 400))

cv2.imshow("image", image)
cv2.imshow("dst1- forward mapping", dst1)
cv2.imshow("dst2- NN interplotaion", dst2)
cv2.waitKey(0)