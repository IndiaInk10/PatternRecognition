import numpy as np, cv2
import resources.draw_histogram as dh

image = cv2.imread("../../resources/images6/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)
image2 = np.zeros(image.shape[:2], image.dtype)
image3 = np.zeros(image.shape[:2], image.dtype)

max = np.max(image)
min = np.min(image)

for h in range(image2.shape[0]):
    for w in range(image2.shape[1]):
        image2[h][w] = image[h][w] - min
        image2[h][w] *= 255 / (max - min)
cv2.normalize(image, image3, min, max, cv2.NORM_MINMAX)

print(np.array_equal(image, image3))
cv2.imshow('histogram1', dh.draw_histo(image))
cv2.imshow('histogram1', dh.draw_histo(image3))
cv2.imshow("origin", image)
cv2.imshow("modify1", image2)
cv2.imshow("modify2", image3)
cv2.waitKey(0)