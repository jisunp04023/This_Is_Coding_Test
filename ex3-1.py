# 예제 3-1
"""
거스름돈 500원, 100원, 50원, 10원 무한히 존재
손님에게 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야 할 동전의 최소 개수를 구하라.
N은 항상 10의 배수
"""
n = int(input())

coin = [500, 100, 50, 10]
count = 0

for i in coin:
    count += (n // i)
    n = n % i

print(count)
