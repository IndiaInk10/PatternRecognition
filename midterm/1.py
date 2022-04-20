# Nearest resize 함수 완성하기

import numpy as np, cv2


def my_resize(logo, dsize, fx=0.0, fy=0.0):
    originY = logo.shape[0]
    originX = logo.shape[1]

    # tuple에서 list로 변환
    dsize = list(dsize)
    # 둘 중에 하나라도 0이 아니라면
    if dsize[0] * dsize[1] != 0:
        # X, Y 값이기 때문에 Y, X로 변환해서 행렬에서 사용
        dsize[0], dsize[1] = dsize[1], dsize[0]
    else:
        # 둘 다 0이라면 원래 값에서 해당 비율 늘리거나 줄이기
        dsize[0] = round(originY * fy)
        dsize[1] = round(originX * fx)
    # 3차원
    dsize.append(3)
    dsize = tuple(dsize)
    logoTemp = np.zeros(dsize, image.dtype)

    for h in range(0, logoTemp.shape[0]):
        for w in range(0, logoTemp.shape[1]):
            # 각 좌표에 상대적으로 대응되는 좌표로 b g r값 넣어주기
            logoTemp[h][w][0] = logo[h * originY // dsize[0]][w * originX // dsize[1]][0]
            logoTemp[h][w][1] = logo[h * originY // dsize[0]][w * originX // dsize[1]][1]
            logoTemp[h][w][2] = logo[h * originY // dsize[0]][w * originX // dsize[1]][2]

    logo = logoTemp
    return logo


image = cv2.imread("images/write_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

X = 0
Y = 0
Fx = 0.0
Fy = 0.0

while True:
    X = int(input())
    Y = int(input())
    Fx = float(input())
    Fy = float(input())

    # 하나라도 음수가 입력되면 종료
    if X < 0 or Y < 0 or Fx < 0 or Fy < 0: break
    
    img2 = cv2.resize(image, (X, Y), fx=Fx, fy=Fy, interpolation=cv2.INTER_NEAREST)
    img3 = my_resize(image, (X, Y), fx=Fx, fy=Fy)

    cv2.imshow("opencvresize", img2)
    cv2.imshow("userresize", img3)

    cv2.waitKey(0)
