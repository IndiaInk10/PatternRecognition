# define function and use
def calc_area(type, a, b, c=None):  # None으로 생략가능하게 설정
    if type == 1:
        result = a * b
        msg = '사각형'
    elif type == 2:
        result = a * b / 2
        msg = '삼각형'
    elif type == 3:
        result = (a + b) * c / 2
        msg = '사다리꼴'
    return result, msg  # return이 2이상인 경우 tuple로 return

def say():
    print('넓이를 구해요')

def write(result, msg):
    print(msg + '의', '넓이는', str(result) + 'm**2 입니다.')
