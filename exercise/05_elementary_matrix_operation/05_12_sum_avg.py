import numpy as np, cv2

image = cv2.imread("../../resources/images_5/sum_test.jpg", cv2.IMREAD_COLOR)

mask = np.zeros(image.shape[:2], np.uint8) # 읽어온 이미지만한 사이즈
mask[60:160, 20:120] = 255

# 채널별 합, 튜플로 반환
sum_value = cv2.sumElems(image)
# 채널별 평균, 튜플로 반환
mean_value1 = cv2.mean(image)
mean_value2 = cv2.mean(image, mask)

print("sum_value 자료형:", type(sum_value), type(sum_value[0]))
print("[sum_value] = ", sum_value)
print("[mean_value1] = ", mean_value1)
print("[mean_value2] = ", mean_value2)
print()

mean, stddev = cv2.meanStdDev(image)
mean2, stddev2 = cv2.meanStdDev(image, mask=mask)
print("mean 자료형:", type(mean), type(mean[0][0]))
print("[mean] =", mean.flatten())
print("[Stddev] =", stddev.flatten())
print()

print("[mea2n] =", mean2.flatten())
print("[Stddev2] =", stddev2.flatten())

cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.waitKey(0)