import numpy as np, cv2

image = cv2.imread("../../resources/images07/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0,1,0],
                 [1,1,1],
                 [0,1,0]]).astype('uint8')
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]


dst1 = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask)

cv2.imshow("image", image)
cv2.imshow("Opening", dst1)
cv2.imshow("Closing", dst2)
cv2.waitKey(0)