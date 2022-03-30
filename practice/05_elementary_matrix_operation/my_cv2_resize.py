import numpy as np, cv2

image = cv2.imread("../../resources/images_4/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("파일 에러")

image2 = cv2.resize(image, (image.shape[1]*2,image.shape[0]*2), interpolation= cv2.INTER_NEAREST)
image3 = np.zeros((image.shape[0]*2,image.shape[1]*2, 3), image.dtype)
# image3을 작업해서 image2랑 같은 결과가 나오도록
for h in range(0, image3.shape[0]):
    for w in range(0, image3.shape[1]):
        image3[h][w][0] = image[h // 2][w // 2][0]
        image3[h][w][1] = image[h // 2][w // 2][1]
        image3[h][w][2] = image[h // 2][w // 2][2]

cv2.imshow("inter1", image2)
cv2.imshow("inter2", image3)

cv2.waitKey(0)