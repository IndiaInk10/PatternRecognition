import cv2
import numpy as np, math
import scipy.fftpack as sf


def exp(knN):
    th = -2 * math.pi * knN
    return complex(math.cos(th), math.sin(th))              # 복소수 클래스


def dft(g):
    N = len(g)
    dst = [sum(g[n] * exp(k*n/N ) for n in range(N)) for k in range(N) ]
    return np.array(dst)


def idft(g):
    N = len(g)
    dst = [sum(g[n] * exp(-k*n/N) for n in range(N)) for k in range(N) ]
    return np.array(dst) / N


def calc_spectrum(complex):
    if complex.ndim == 2:
        dst = abs(complex)
    else:
        dst = cv2.magnitude(complex[:,:,0], complex[:,:,1])
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)


def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h//2, w//2
    dst[h-cy:,w-cx:] = np.copy(img[0:cy,0:cx])
    dst[0:cy, 0:cx] = np.copy(img[h-cy:,w-cx:])
    dst[0:cy, w-cx:] = np.copy(img[h-cy:,0:cx])
    dst[h-cy:, 0:cx] = np.copy(img[0:cy,w-cx:])
    return dst


def zeropadding(img):
    h,w = img.shape[:2]
    m = 1 << int(np.ceil(np.log2(h)))
    n = 1 << int(np.ceil(np.log2(w)))
    dst = np.zeros((m,n), img.dtype)
    dst[0:h,0:w] = img[:]
    return dst


def butterfly(pair, L, N, dir):
    for k in range(L):                                       # 버터플라이 수행
        Geven, Godd = pair[k], pair[k + L]
        pair[k]     = Geven + Godd * exp(dir * k / N)       # 짝수부
        pair[k + L] = Geven - Godd * exp(dir * k / N)       # 홀수부


def pairing(g, N, dir, start=0, stride=1):
    if N == 1: return [g[start]]
    L = N // 2
    sd = stride * 2
    part1 = pairing(g, L, dir, start, sd)
    part2 = pairing(g, L, dir, start + stride, sd)
    pair = part1 + part2                                     # 결과 병합
    butterfly(pair, L, N, dir)
    return pair


def fft(g):
    return pairing(g, len(g), 1)


def ifft(g):
    fft = pairing(g, len(g), -1)
    return [v / len(g) for v in fft]


def fft2(image):
    pad_img = zeropadding(image)  # 영삽입
    tmp = [fft(row) for row in pad_img]
    dst = [fft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)                        # 전치 환원 후 반환


def ifft2(image):
    tmp = [ifft(row) for row in image]
    dst = [ifft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)                        # 전치 환원 후 반환


def FFT(image, mode = 2):
    if mode == 1: dft = fft2(image)
    elif mode==2: dft = np.fft.fft2(image)
    elif mode==3: dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft = fftshift(dft)                              # 셔플링
    spectrum = calc_spectrum(dft)               # 주파수 스펙트럼 영상
    return dft, spectrum


def IFFT(dft, shape, mode=2):
    dft = fftshift(dft)                                 # 역 셔플링
    if mode == 1: img = ifft2(dft).real
    if mode == 2: img = np.fft.ifft2(dft).real
    if mode ==3:  img = cv2.idft(dft, flags= cv2.DFT_SCALE)[:,:,0]
    img = img[:shape[0], :shape[1]]                 # 영삽입 부분 제거
    return cv2.convertScaleAbs(img)


def cos(n, k, N):
    return math.cos((n+1/2) * math.pi * k/N)


def C(k, N):
    return math.sqrt(1/N) if k==0 else math.sqrt(2/N)


def dct(g):
    N = len(g)
    f = [C(k,N) * sum(g[n] * cos(n, k, N) for n in range(N)) for k in range(N)]
    return np.array(f, np.float32)

def idct(f):
    N = len(f)
    g = [sum(C(k, N) * f[k] * cos(n, k, N) for k in range(N)) for n in range(N)]
    return np.array(g)


def dct2(image):
    tmp = [dct(row) for row in image]
    dst = [dct(row) for row in np.transpose(tmp)]
    return np.transpose(dst)


def idct2(image):
    tmp = [idct(row) for row in image]
    dst = [idct(row) for row in np.transpose(tmp)]
    return np.transpose(dst)


def scipy_dct2(a):
    tmp = sf.dct(a, axis=0, norm='ortho')
    return sf.dct(tmp, axis=1, norm='ortho')


def scipy_idct2(a):
    tmp = sf.idct(a, axis=0, norm='ortho')
    return sf.idct(tmp, axis=1, norm='ortho')