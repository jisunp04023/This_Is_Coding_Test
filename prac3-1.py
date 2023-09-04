# 실전 3-1
"""
큰 수의 법칙
주어진 수를 M번 더하여 가장 큰 수를 만드는 방법.
배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수는 없다.

첫째 줄에 N, M, K의 자연수가 주어진다.
둘째 줄에 N개의 자연수가 주어진다.
입력이 주어지는 K는 항상 M보다 작거나 같다. (K <= M)
첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
"""
n, m, k = map(int, input().split())
l = list(map(int, input().split()))

l.sort()

s = 0

while True:
    for i in range(k):
        if not m:
            break
        s += l[-1]
        m -= 1

    if not m:
        break
    s += l[-2]
    m -= 1

print(s)
