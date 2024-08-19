# 2741 N_찍기
'''
count = int(input())

for i in range(count):
    print(i+1)
'''
# 10872 팩토리얼
'''
fac = int(input())

if fac == 1:
    print("1")
else:
    result = 1
    for i in range(1,fac+1):
        result *= i
    print(result)
'''
# 10950 A+B -3
'''
case = int(input())

for i in range(1,case+1):
    a, b = map(int, input().split())
    print(a+b)
'''
# 10952 A+B -5
'''
while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
'''
# 2739 구구단
'''
gugudan = int(input())

for i in range(1,10):
    print(f'{gugudan} * {i} = {gugudan * i}')
'''
# 2438 별찍기 -1
'''
starCount = int(input())

for i in range(starCount):
    print("*" * (i+1))
'''
# 10951 A+B -4
'''
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
'''