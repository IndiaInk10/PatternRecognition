import cv2

image = cv2.imread("../resources/images_4/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]

## 행렬을 영상파일로 저장
cv2.imwrite("../resources/images_4/after/write_test1.jpg", image)
cv2.imwrite("../resources/images_4/after/write_test2.jpg", image, params_jpg)
cv2.imwrite("../resources/images_4/after/write_test3.png", image, params_png)
cv2.imwrite("../resources/images_4/after/write_test4.bmp", image)
cv2.imwrite("../resources/images_4/after/image_test5.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 100))
cv2.imwrite("../resources/images_4/after/image_test6.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 70))
cv2.imwrite("../resources/images_4/after/image_test7.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 40))
cv2.imwrite("../resources/images_4/after/image_test8.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 10))
print("저장 완료")