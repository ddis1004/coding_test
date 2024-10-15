import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for a in A:
    answer += 1
    a -= B
    if a < 0:
        continue
    else:
        answer += math.ceil(a / C)

print(answer)
