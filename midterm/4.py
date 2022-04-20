# 워터마크
import numpy as np, cv2, math

while(True):
    logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
    bgImg = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)
    if bgImg is None or logo is None: raise Exception("영상파일 읽기 오류")

    width = int(input('가로에 들어갈 개수를 입력하시오.'))
    height = int(input('세로에 들어갈 개수를 입력하시오.'))
    
    # 가로, 세로 0 또는 음수 입력시 종료
    if width <= 0 or height <= 0: break

    # 개수만큼 들어갈 수 있게 logo 이미지 사이즈 조정
    # round 하게 되면 범위초과되는 경우가 생길 수 있어서 floor
    resizeY = math.floor(bgImg.shape[0] / height)
    resizeX = math.floor(bgImg.shape[1] / width)

    logo = cv2.resize(logo, (resizeX, resizeY), interpolation=cv2.INTER_LINEAR)

    # mask 만들기
    masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1] # 220 <=
    masks = cv2.split(masks)

    fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
    fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
    bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

    (H, W), (h, w) = bgImg.shape[:2], logo.shape[:2]
    # logo 사이의 간격을 줄 수도 있게 padding값을 선언 및 정의
    padding = 0

    for yStart in range(0, H, h + padding):
        # logo의 세로 끝범위
        yEnd = (yStart + h)
        if yEnd > bgImg.shape[0]: break
        for xStart in range(0, W, w + padding):
            # logo의 가로 끝범위
            xEnd = (xStart + w)
            if xEnd > bgImg.shape[1]: break

            # bgImg에서 워터마크 저장할 부분만 가져오기
            roi = bgImg[yStart:yEnd, xStart:xEnd]
            foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
            # bit연산으로 뚫고
            background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

            # logo 삽입
            dst = cv2.add(background, logo)
            bgImg[yStart:yEnd, xStart:xEnd] = dst

    cv2.imshow('background', bgImg)
    cv2.imshow('logo', logo)
    cv2.waitKey(0)