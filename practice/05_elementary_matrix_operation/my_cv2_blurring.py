import numpy as np, cv2

image = cv2.imread("../../resources/images_5/color.jpg", cv2.IMREAD_COLOR)
image_temp = image
image_blur = cv2.blur(image, (5,5))

# 사이드의 기준은 짤리는거 제외 2칸으로 가져가기
for i in range(2, image_temp.shape[0] - 2):
    for j in range(2, image_temp.shape[1] - 2):
        # 원본에서는 추출만하고 이후 가공하고 다시 합체 또는 복사된 녀석에게 적용
        m = image[i-2:i+3, j-2:j+3] # filter
        # image_temp[i][j][0] = cv2.mean(m)[0]
        # image_temp[i][j][1] = cv2.mean(m)[1]
        # image_temp[i][j][2] = cv2.mean(m)[2]
        reduce_y = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG)
        reduce_x = cv2.reduce(reduce_y, dim=0, rtype=cv2.REDUCE_AVG)
        # image_temp[i-2:i+3, j-2:j+3] = reduce_x 가
        # 안되는 이유는 바로 픽셀 하나 하나를 범위를 가지고 평균을 내서 지정
        image_temp[i, j] = reduce_x

cv2.imshow("blur", image_temp)
cv2.imshow("blur2", image_blur)

cv2.waitKeyEx()