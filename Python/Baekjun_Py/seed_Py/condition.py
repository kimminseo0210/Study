# 1330 두 수 비교하기
'''
a,b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')
'''

# 9498 시험 성적
'''
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
'''

# 14681 사분면 고르기
'''
x = int(input())
y = int(input())
# map을 사용하면 런타임에러(vlaue error)가 발생함

if x>0 and y>0 :
    print('1')
elif x<0 and y>0 :
    print('2')
elif x<0 and y<0 :
    print('3')
elif x>0 and y<0 :
    print('4')
'''

# 2753 윤년
'''
year = int(input()) # 년도 입력

if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    print("1")
else:
    print("0")
'''

# 2420 사파리 월드
'''
a, b = map(int, input().split())
print(abs(a-b))
'''