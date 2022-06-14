import numpy as np, cv2

def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows,cols), np.float32)
    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    for i in range(ycenter, rows-ycenter):
        for j in range(xcenter, cols-xcenter):
            y1,y2 = i - ycenter, i + ycenter + 1
            x1,x2 = j - xcenter, j + xcenter + 1
            roi = image[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i,j] = cv2.sumElems(tmp)[0]
    return dst

def filter2(image, mask):
    rows,cols = image.shape[:2]
    dst = np.zeros((rows,cols), np.float32)
    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    for i in range(ycenter, rows-ycenter):
        for j in range(xcenter, cols-xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y,x = i + u - ycenter, j + v - xcenter
                    sum += image[y,x] * mask[u,v]
            dst[i,j] = sum
    return dst

image = cv2.imread("../../resources/images07/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data = [ 1/9, 1/9, 1/9,
         1/9, 1/9, 1/9,
         1/9, 1/9, 1/9 ]
mask = np.array(data, np.float32).reshape(3,3)

blur1 = filter(image, mask)
blur2 = filter2(image, mask)
# 동일한 데이터 셋으로 출력
blur3 = cv2.filter2D(image, -1, mask)
cv2.imshow("blur3", blur3)
blur1 = blur1.astype('uint8')
blur2 = cv2.convertScaleAbs(blur2)

cv2.imshow("image", image)
cv2.imshow("blur1", blur1)
cv2.imshow("blur2", blur2)
cv2.waitKey(0)