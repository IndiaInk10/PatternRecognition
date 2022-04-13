import numpy as np, cv2
import resources.draw_histogram as dh

image = cv2.imread("../../resources/images6/draw_hist.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("../../resources/images6/hue_hist.jpg", cv2.IMREAD_COLOR)
if image is None or image2 is None: raise Exception("영상파일 읽기 오류")

histSize, ranges = [32], [0, 256]
gap = ranges[1] / histSize[0]
ranges_gap = np.arange(0, ranges[1]+1, gap)
hist = cv2.calcHist([image], [0], None, histSize, ranges)
hist2, bins = np.histogram(image, ranges_gap)

hsv_img = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
hue_hist = cv2.calcHist([hsv_img], [0], None, [18], [0,180])

print("OpenCV 함수: \n", hist.flatten())
print("numpy 함수: \n", hist2)
cv2.imshow("image", image)
cv2.imshow("image", image2)
cv2.imshow("histogram", dh.draw_histo(hist))
cv2.imshow("histogram2", dh.draw_histo(hist2))
cv2.imshow("histogram3", dh.draw_hist_hue(hue_hist, (200,360, 3)))
cv2.waitKey(0)