import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255) # BGR(0,0,0)
image = np.zeros((400, 600, 3), np.uint8)   # three-dimensional image
image[:] = (255, 255, 255)

# tuples, const list
pt1, pt2 = (50, 50), (250, 150)
pt3, pt4 = (400, 150), (500, 50)
roi = (50, 200, 200, 100)

## draw line
cv2.line(image, pt1, pt2, red)
# cv2.line(multi-dimensional_list_name, coordXY1, coordXY2, color, thickness, option)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA)    # cv2.LINE_AA == anti-aliasing

## draw rect
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)
cv2.rectangle(image, (400, 200, 100, 100), green, cv2.FILLED)

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
