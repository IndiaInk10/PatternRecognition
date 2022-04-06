import numpy as np, cv2

image = cv2.imread("../../resources/images_5/minMax.jpg", cv2.IMREAD_GRAYSCALE)

min_val, max_val,_,_ = cv2.minMaxLoc(image)

# 전체적인 밝기 증가
ratio = 255 / (max_val - min_val)
dst = np.round((image - min_val) * ratio).astype('uint8')
min_dst, max_dst,_,_ = cv2.minMaxLoc(dst)

print("원본 영상 최솟값 = %d, 최댓값 = %d" %(min_val, max_val))
print("수정 영상의 최솟값 = %d, 최댓값 = %d" %(min_dst, max_dst))
cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)
