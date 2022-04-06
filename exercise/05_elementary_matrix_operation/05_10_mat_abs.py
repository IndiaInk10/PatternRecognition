import numpy as np, cv2

image1 = cv2.imread("../../resources/images_5/abs_test1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("../../resources/images_5/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)

dif_img1 = cv2.subtract(image1, image2)
dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2))
abs_dif1 = np.absolute(dif_img2).astype('uint8')
abs_dif2 = cv2.absdiff(image1, image2)

x, y, w, h = 100, 150 , 7, 3

titles = ['image1', 'image2', 'dif_img1', 'abs_dif1', 'abs_dif2']
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)