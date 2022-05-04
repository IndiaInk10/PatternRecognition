import numpy as np, cv2

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3,3)
    mask2 = np.array(data2, np.float32).reshape(3,3)

    dst1 = cv2.filter2D(image.astype("float32"), -1, mask1)
    dst2 = cv2.filter2D(image.astype("float32"), -1, mask2)
    dst = cv2.magnitude(dst1, dst2)

    dst = np.clip(dst, 0, 255).astype('uint8')
    dst1 = np.clip(dst1, 0, 255).astype('uint8')
    dst2 = np.clip(dst2, 0, 255).astype('uint8')

    return dst, dst1, dst2

image = cv2.imread("../../resources/images07/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 0,
         0, 1, 0,
         0, 0, 0]
data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]

dst, dst1, dst2 = differential(image, data1, data2)

cv2.imshow("image", image)
cv2.imshow("roberts edge", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)