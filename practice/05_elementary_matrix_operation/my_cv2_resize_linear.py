# 중간고사 1번 과제
import numpy as np, cv2
import math

image = cv2.imread("../../resources/images_4/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("파일 에러")
print(image.shape)
originY = image.shape[0]
originX = image.shape[1]

X = 500
Y = 700

# image2 = cv2.resize(image, (image.shape[1]*2,image.shape[0]*2), interpolation= cv2.INTER_LINEAR)
image2 = cv2.resize(image, (X, Y), interpolation= cv2.INTER_LINEAR)
# image3 = np.zeros((image.shape[0]*2,image.shape[1]*2, 3), image.dtype)
image3 = np.zeros((Y, X, 3), image.dtype)

for h in range(0, image3.shape[0]):
    for w in range(0, image3.shape[1]):
        # image3[h][w][0] = cv2.reduce(image[math.floor(h * originY / Y)]
        #                              [math.floor(w * originX / X): math.ceil(w * originX / X)][0]
        #                              , dim=0, rtype=cv2.REDUCE_AVG)
        # image3[h][w][1] = cv2.reduce(image[math.floor(h * originY / Y)]
        #                              [math.floor(w * originX / X): math.ceil(w * originX / X)][1]
        #                              , dim=0, rtype=cv2.REDUCE_AVG)
        # image3[h][w][2] = cv2.reduce(image[math.floor(h * originY / Y)]
        #                              [math.floor(w * originX / X): math.ceil(w * originX / X)][2]
        #                              , dim=0, rtype=cv2.REDUCE_AVG)
        # print(math.floor(w * originX / X), math.ceil(w * originX / X))
        # if math.floor(w * originX / X) == math.ceil(w * originX / X):
        #     w = math.floor(w * originX / X)
        #     image3[h][w][0] = image[h * originY // Y][w][0]
        #     image3[h][w][1] = image[h * originY // Y][w][1]
        #     image3[h][w][2] = image[h * originY // Y][w][2]
        # else:
        #     image3[h][w][0] = cv2.reduce(image[math.floor(h * originY / Y), 0, math.floor(w * originX / X): math.ceil(w * originX / X) + 1], dim=0, rtype=cv2.REDUCE_AVG)
        #     image3[h][w][1] = cv2.reduce(image[math.floor(h * originY / Y), 0, math.floor(w * originX / X): math.ceil(w * originX / X) + 1], dim=0, rtype=cv2.REDUCE_AVG)
        #     image3[h][w][2] = cv2.reduce(image[math.floor(h * originY / Y), 0, math.floor(w * originX / X): math.ceil(w * originX / X) + 1], dim=0, rtype=cv2.REDUCE_AVG)

        image3[h][w][0] = image[h * originY // Y][w * originX // X][0]
        image3[h][w][1] = image[h * originY // Y][w * originX // X][1]
        image3[h][w][2] = image[h * originY // Y][w * originX // X][2]

cv2.imshow("inter1", image2)
cv2.imshow("inter2", image3)

cv2.waitKey(0)

