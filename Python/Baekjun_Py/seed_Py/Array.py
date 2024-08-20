# 10871 X 보다 작은 수
'''
ArrayNum, count = map(int, input().split())

A = list(map(int, input().split()))

for i in range(ArrayNum):
    if A[i] < count:
        print(A[i])
'''
# 10807 개수 세기
'''
Num = int(input())
Arr = list(map(int, input().split()))
Find = int(input())

count = 0

for i in Arr:
    if i == Find:
        count += 1
print(count)
'''
# 5597 과제 안 내신 분..?



# 2739 행렬 덧셈