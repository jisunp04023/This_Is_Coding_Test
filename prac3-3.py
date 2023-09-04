# 실전 3-3
"""
n이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행.
두번째 연산은 n이 k로 나누어 떨어질 때만 선택 가능.

1. n에서 1을 뺀다.
2. n을 k로 나눈다.

n이 1이 될 때까지 1번 혹은 2번을 수행하는 최소 횟수를 구하라.

첫째 줄에 n, k가 주어짐 (n >= k)
"""

n, k = map(int, input().split())

cnt = 0

while True:
    if n == 1:
        break

    if n % k: # n이 k로 나누어 떨어지지 않을 경우
        n -= 1
        cnt += 1
    else:
        n = n / k
        cnt += 1

print(cnt)
