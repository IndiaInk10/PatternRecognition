import numpy as np, cv2

image = cv2.imread("../../resources/images_5/bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("../../resources/images_5/logo.jpg", cv2.IMREAD_COLOR)
if image is None or logo is None: raise Exception("영상파일 읽기 오류")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1] # 220 <=
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W - w)//2 , (H - h)//2
print(H,W)
print(h,w)


padding = 10

for yStart in range(0, H, h + padding):
    for xStart in range(0, W, w + padding):
        yEnd = (yStart + h)%H
        if yEnd < yStart: yEnd += yStart - padding
        xEnd = (xStart +w)%W
        if xEnd < xStart: xEnd += xStart - padding
        roi = image[yStart:yEnd, xStart:xEnd]

        # 추출한 이미지에 맞게 조절
        newLogo = logo[:roi.shape[0], :roi.shape[1]]
        # bit연산하는 행렬끼리 사이즈를 맞춰주어야함
        foreground = cv2.bitwise_and(newLogo, newLogo, mask=fg_pass_mask[:roi.shape[0], :roi.shape[1]])
        background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask[:roi.shape[0], :roi.shape[1]])
        dst = cv2.add(background, foreground)

        cv2.waitKey(0)

        image[yStart:yEnd, xStart:xEnd] = dst

# roi = image[y:y+h, x:x+w]
#
# foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
# background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)
#
# dst = cv2.add(background, foreground)
# image[y:y+h, x:x+w] = dst

cv2.imshow('background', background); cv2.imshow('foreground', foreground)
cv2.imshow('dst', dst);               cv2.imshow('image', image)
cv2.waitKey(0)