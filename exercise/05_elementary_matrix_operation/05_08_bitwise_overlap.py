import numpy as np, cv2

image = cv2.imread("../../resources/images_5/bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("../../resources/images_5/logo.jpg", cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception("영상파일 읽기 오류")

# threshold = 220을 못 넘으면 0, 넘으면 255라는 값을 줘서 경계를 명확하게 해준다
masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1] # 220 <=
masks = cv2.split(masks)

# or을 통해서 모든 녀석들을 합쳐준다
fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
# 그리고 바탕은 로고의 반대를 줘서 값을 받을 수 있게 해준다
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W - w)//2 , (H - h)//2  # center
roi = image[y:y+h, x:x+w]

# 로고를 명확하게 해주는 부분
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
# 해당 부분의 배경을 빵꾸내주는 부분, 0로 값으로 빵꾸를 내준다
background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

# 그리고 두 행렬을 합쳐서 로고를 삽입해준다
dst = cv2.add(background, foreground)
image[y:y+h, x:x+w] = dst

cv2.imshow('background', background); cv2.imshow('foreground', foreground)
cv2.imshow('dst', dst);               cv2.imshow('image', image)
cv2.waitKey(0)