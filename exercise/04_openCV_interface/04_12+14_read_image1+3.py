import cv2

def print_matInfo(name, image):
    if image.dtype == 'uint8': mat_type = 'CV_8U'
    elif image.dtype == 'int8': mat_type = 'CV_8S'
    elif image.dtype == 'uint16': mat_type = 'CV_16U'
    elif image.dtype == 'int16': mat_type = 'CV_16S'
    elif image.dtype == 'float32': mat_type = 'CV_32F'
    elif image.dtype == 'float64': mat_type = 'CV_64F'
    nchannel = 3 if image.ndim == 3 else 1

    ## print depth, channel
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type, nchannel))

title1, title2 = '16bit unchanged', '32bit unchanged'
color2unchanged1 = cv2.imread("../resources/images_4/read_16.tif", cv2.IMREAD_UNCHANGED)
color2unchanged2 = cv2.imread("../resources/images_4/read_32.tif", cv2.IMREAD_UNCHANGED)
if color2unchanged1 is None or color2unchanged2 is None:
    raise Exception("영상파일 읽기 에러")

print("16/32비트 영상 행렬 좌표(10,10) 화소값")
print(title1, '원소 자료형 ', type(color2unchanged1[10][10][0]))
print(title1, '화소값(3원소) ', color2unchanged1[10, 10])
print(title2, '원소 자료형 ', type(color2unchanged2[10][10][0]))
print(title2, '화소값(3원소) ', color2unchanged2[10, 10])
print()

print_matInfo(title1, color2unchanged1)
print_matInfo(title2, color2unchanged2)
cv2.imshow(title1, color2unchanged1)
cv2.imshow(title2, (color2unchanged2*255).astype('uint8'))
cv2.waitKey(0)