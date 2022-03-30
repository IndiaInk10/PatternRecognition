import numpy as np
# 1
list1, list2 = [1, 2, 3], [4, 5.0, 6]
a, b = np.array(list1), np.array(list2)

c = a + b
d = a - b
e = a * b
f = a / b
g = a * 2
h = b + 2

print('a 자료형:', type(a), type(a[0]))
print('b 자료형:', type(b), type(b[0]))
print('c 자료형:', type(c), type(c[0]))
print('g 자료형:', type(g), type(g[0]))

print(c, d, e)
print(f, g, h)

# 2
a = np.zeros((2, 5), np.int_)  # zeroVector, [2][5], 32bits int
b = np.ones((3, 1), np.int_)  # oneVector(normalVector), [3][1], unsigned 8bits int
c = np.empty((1, 5), np.float_)  # none value, [1][5]
d = np.full(5, 15, np.float32)  # 15, [1][5], 32bits float

print(type(a), type(a[0]), type(a[0][0]))
print(type(b), type(b[0]), type(b[0][0]))
print(type(c), type(c[0]), type(c[0][0]))
print(type(d), type(d[0]))
print('c 형태:', c.shape, ' d 형태:', d.shape)
print(a), print(b)
print(c), print(d)

# 3
np.random.seed(10)  # setting random seed
a = np.random.rand(2, 3)  # float of 0~1, [2][3]
b = np.random.randn(3, 2)  # normalized of -1~1, [3][2]
c = np.random.rand(6)  # float of 0~1, [1][6]
d = np.random.randint(1, 100, 6)  # int of 1~100, [1][6]
c = np.reshape(c, (2, 3))  # [1][6] to [2][3]
d = d.reshape(2, -1)  # [1][6] to [2][?], -1은 알아서 행이나 열을 계산

print('a 형태:', a.shape, '\n', a)
print('b 형태:', b.shape, '\n', b)
print('c 형태:', c.shape, '\n', c)
print('d 형태:', d.shape, '\n', d)

print('다차원 객체 1차원 변환 방법')
print('a =', a.flatten())  # multi-demension ndarray to one-demension vector
print('b =', np.ravel(b))  # Any multi-demension to one-demension vector
print('c =', np.reshape(c, (-1, )))  # reshape, if second factor is empty that means i want to make one-demension
print('d =', d.reshape(-1, ))  # ndarray's reshape