import numpy as np, cv2, math, random

# 이미지 위에 샘플 위치를 그려주는 함수
def draw_points(image, group, color):
    for p in group:
        pt = tuple(p.astype(int))
        cv2.circle(image, pt, 3, color, cv2.FILLED)

# 이미지 위에 군집 위치를 그려주는 함수
def draw_cluster(image, cluster, color):
    global K
    for i in range(0, K):
        clusterLine1 = [[cluster[i][0] + 4, cluster[i][1] + 4], [cluster[i][0] - 4, cluster[i][1] - 4]]
        clusterLine2 = [[cluster[i][0] - 4, cluster[i][1] + 4], [cluster[i][0] + 4, cluster[i][1] - 4]]
        cv2.line(image, clusterLine1[0], clusterLine1[1], color=color[i], thickness=2)
        cv2.line(image, clusterLine2[0], clusterLine2[1], color=color[i], thickness=2)

# 군집화가 끝났을 경우, 결과창 그려주는 함수
def draw_end(image, clusters, colors, nCluster, count):
    for j in range(0, K):
        draw_points(image, clusters[j][:], color=colors[j])
    draw_cluster(image, nCluster, colors)
    cv2.putText(image, f"{K}-means clustering End(loop:{count})", (230, 500), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

# 두 점 사이의 거리를 구해주는 함수
def get_distance(pt1, pt2):
    return math.sqrt(math.pow(pt1[0] - pt2[0], 2) + math.pow(pt1[1] - pt2[1], 2))


initImage = np.zeros((1002,1002,3), dtype="uint8")

# red = (0, 0, 255)
# green = (0, 255, 0)
# yellow = (0, 255, 255)
# colors = [red, green, yellow]

K = 3
nSample = 100

# 샘플 랜덤값 설정
nData = np.zeros((nSample, 2), np.float32)
for i in range(0, nSample):
    nData[i,0] = random.randrange(1, 1001)
    nData[i,1] = random.randrange(1, 1001)

colors = []
nCluster = []
# 각 군집 초기 위치 설정
for i in range(0, K):
    colors.append((random.randrange(10, 256), random.randrange(10, 256), random.randrange(10, 256)))
    nCluster.append([random.randrange(1, 1001), random.randrange(1, 1001)])

before = np.zeros(0)
clusters = [[]]
isEnd = False
# 군집화 시작
for i in range(0, 100):
    image = initImage.copy()

    if clusters[0]:
        for j in range(0, K):
            mean = list(map(int, np.mean(clusters[j], axis=0)))
            # 각 군집이 이전 위치와 동일한 경우, 군집화를 종료
            if mean[0:1] == nCluster[j][0:1] and j == K - 1:
                isEnd = True
                draw_end(image, clusters, colors, nCluster, i)

            nCluster[j][0] = mean[0]
            nCluster[j][1] = mean[1]

    if isEnd:
        break

    draw_cluster(image, nCluster, colors)

    clusters = np.zeros((K, 0), dtype="int_").tolist()

    for j in range(0, nSample):
        minDistance = []
        for k in range(0, K):
            minDistance.append(get_distance(nCluster[k], nData[j]))
        # K개의 군집에 대한 거리를 재고, 최소거리에 해당하는 index에 맞는 군집에 해당 data를 추가(ex: index = 0, 0번째 군집에 추가)
        clusters[minDistance.index(min(minDistance))].append(nData[j])

    # 각 군집의 색으로 포함된 샘플들을 그림
    for j in range(0, K):
        draw_points(image, clusters[j][:], color=colors[j])

    if i == 0:
        before = image.copy()

    cv2.imshow(f"After {K}-means clustering", image)
    cv2.waitKey(0)

cv2.imshow(f"Before {K}-means clustering", before)
cv2.imshow(f"After {K}-means clustering", image)
cv2.waitKey(0)