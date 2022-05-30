import numpy as np, cv2, math, random


def draw_points(image, group, color):
    for p in group:
        pt = tuple(p.astype(int))
        cv2.circle(image, pt, 3, color, cv2.FILLED)


def draw_cluster(image, cluster, color):
    clusterLine1 = [[cluster[0] + 4, cluster[1] + 4], [cluster[0] - 4, cluster[1] - 4]]
    clusterLine2 = [[cluster[0] - 4, cluster[1] + 4], [cluster[0] + 4, cluster[1] - 4]]
    cv2.line(image, clusterLine1[0], clusterLine1[1], color=color, thickness=2)
    cv2.line(image, clusterLine2[0], clusterLine2[1], color=color, thickness=2)


def get_distance(pt1, pt2):
    return math.sqrt(math.pow(pt1[0] - pt2[0], 2) + math.pow(pt1[1] - pt2[1], 2))


image = np.zeros((1002,1002,3), dtype="uint8")

red = (0, 0, 255)
green = (0, 255, 0)
yellow = (0, 255, 255)
colors = [red, green, yellow]

nSample = 100
nData = np.zeros((nSample, 2), np.float32)

for i in range(0, nSample):
    nData[i,0] = random.randrange(1, 1001)
    nData[i,1] = random.randrange(1, 1001)

K = 3
nCluster = []

for i in range(0, K):
    nCluster.append([random.randrange(1, 1001), random.randrange(1, 1001), []])
    draw_cluster(image, nCluster[i], colors[i])

clusters = [[], [], []]

for i in range(0, nSample):
    minDistance = []
    for j in range(0, K):
        minDistance.append(get_distance(nCluster[j], nData[i]))
    clusters[minDistance.index(min(minDistance))].append(nData[i])

for i in range(0, K):
    draw_points(image, clusters[i][:], color=colors[i])

cv2.imshow("3 means clustering", image)
cv2.waitKey(0)