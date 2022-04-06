# 중간고사 1번 과제
import numpy as np, cv2

image = cv2.imread("../../resources/images_4/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("파일 에러")

x = 200
y = 300

# image2 = cv2.resize(image, (image.shape[1]*2,image.shape[0]*2), interpolation= cv2.INTER_LINEAR)
image2 = cv2.resize(image, (x,y), interpolation= cv2.INTER_LINEAR)
# image3 = np.zeros((image.shape[0]*2,image.shape[1]*2, 3), image.dtype)
image3 = np.zeros((x,y), image.dtype)




cv2.imshow("inter1", image2)
cv2.imshow("inter2", image3)

cv2.waitKey(0)

