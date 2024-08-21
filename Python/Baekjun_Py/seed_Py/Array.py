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
'''
student = []
n_student = []

for i in range(28):
    s = int(input())
    student.append(s)

for i in range(1,31):
    if i not in student:
        n_student.append(i)

print(min(n_student))
print(max(n_student))
'''

# 2739 행렬 덧셈