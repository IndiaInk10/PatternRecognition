
# use const with uppercase words
PI = 3.141592

# auto data type casting variable with input value
variable1 = 100
variable2 = -100
variable3 = 1.0 + 3.0j  # 복소수
# data type casting manually
variable4 = float(variable1)
# print value and data type
print('variable1 = ', variable1, type(variable1))

# data structures
# list == array
list1 = [1, 2, 3, 4]
list2 = [1, 1.5, 'a', 'a', '문자열']
# tuple == const list
tuple1 = (1, 2)
tuple2 = (1, 1.5, 'b', 'b', '문자열')
# dictionary
dict1 = {'name': '배종욱', 'email': 'daum.net'}  # key: value
# set
set1,  set2 = set(list2), set(tuple2)  # 중복 없음, 순서 자기 맘대로

list1[0] = 5
list2.insert(3, 'b')
dict1['email'] = 'naver.com'

print('set1', set1, type(set1))
print('set2', set2, type(set2))
print('intersection', set1 & set2)  # 교집합

# slice operator
a = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
print('a[:2] -> ', a[:2])  # 0~1
print('a[4:-1] -> ', a[4:-1])  # 4~8, -1은 마지막 9
print('a[2::2] -> ', a[2::2])  # 2~9, 짝수
print('a[::-1] -> ', a[::-1])  # (-1 == 역순) 역순에서의 시작위치는 -1, 9~0
print('a[1::-1] -> ', a[1::-1])  # (-1 == 역순) 1~0
print('a[7:1:-2] -> ', a[7:1:-2])  # (-2 == 역순) 7~2, 홀수
print('a[:-4:-1] -> ', a[:-4:-1])  # (-1 == 역순) 역순에서의 시작위치는 -1, 9~7

# if
year = 2020

if(year % 4 == 0) and (year % 100 != 0):
    print(year, "는 윤년입니다.")
elif year % 400 == 0:
    print(year, "는 윤년입니다.")
else:
    print(year, "는 윤년이 아닙니다.")

# while
n = 3
while n >= 3:
    m = input("Enter a integer: ")  # only string input == input
    if int(m) == 0: break
    n = n - 1
else:
    print("4 inputs.")

# for ~ in, loop count == len(list)
# range(start, end, +-), exclude end
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum = 0

for i in range(0, 5):
    sum = sum + kor[i] + eng[i]

sum = 0
for k in kor:
    sum = sum + k
for e in eng:
    sum = sum + e

# enumerate make tuple with index and value
# ex)  enumerate(kor) = (0, 70), (0, 80), (0, 90), ...
sum = 0
for i, k in enumerate(kor):
    sum = sum + eng[i] + k

# zip make tuple with two list's value
# ex) zip(kor, eng) = (70, 90), (80, 80), (90, 70), ...
sum = 0
for k, e in zip(kor, eng):
    sum = sum + k  + e

print('sum = ', sum)

# module == header, library(c)
# import, import ~ as
# from ~ import, from ~ import ~ as / not recommended
import header_area_03_01 as mod  # header_area.py를 module로 import
from header_area_03_01 import write  # header_area.py내의 write function만 import


mod.say()
ret = mod.calc_area(type=1, a=5, b=5)  # return tuple
# return tuple as each value
# ex) return (12.5, '삼각형') area = 12.5, msg = '삼각형'
area, msg = mod.calc_area(2, 5, 5)
# return only what i want at return
# ex) return (42.5, '사다리꼴') area2 = 42.5, _(no need '사다리꼴')
area2, _ = mod.calc_area(3, 10, 7, 5)

print(type(ret))
print(type(area), type(msg))
write(ret[0], ret[1])
write(area, msg)
write(area2, '사다리꼴')
