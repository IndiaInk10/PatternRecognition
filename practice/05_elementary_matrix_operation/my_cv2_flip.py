import numpy as np
import cv2

image = cv2.imread("../../resources/images_5/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("에러")

image_x = np.zeros(image.shape,image.dtype)
image_y = np.zeros(image.shape,image.dtype)
image_xy = np.zeros(image.shape,image.dtype)
image_trans = np.zeros((image.shape[1],image.shape[0],image.shape[2]), image.dtype)

# for문을 통한 flip 구현
for h in range(0, image.shape[0]):
    for w in range(0, image.shape[1]):
        # image_x[h][w] = image[h][-w]
        image_x[h][w] = image[h][image.shape[1] - 1 - w]
        # image_y[h][w] = image[-h][w]
        image_y[h][w] = image[image.shape[0] - 1 - h][w]
        # image_xy[h][w] = image[-h][-w]
        image_xy[h][w] = image[image.shape[0] - 1 - h][image.shape[1] - 1 - w]
        image_trans[w][h] = image[h][w]

# for h in range(0, image_trans.shape[0]):
#    for w in range(0, image_trans.shape[1]):
#        image_trans[h][w] = image[w][h]

cv2.imshow("origianl",image)
cv2.imshow("x_flip",image_x)
cv2.imshow("y_flip",image_y)
cv2.imshow("xy_flip",image_xy)
cv2.imshow("xy_trans",image_trans)


cv2.waitKey(0)


