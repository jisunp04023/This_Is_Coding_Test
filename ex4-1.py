# 예제 4-1
"""
a는 n*n 정사각형 공간 위에 서 있다.
가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (n, n)에 해당됨.
a는 상, 하, 좌, 우 방향으로 이동 가능 (u, d, l, r), 시작좌표는 (1, 1)이다.
정사각형 공간을 벗어나는 움직임은 무시됨.
최종 도착할 지점의 좌표를 출력.

첫째 줄에는 n, 둘째 줄에는 a가 이동할 계획서가 주어짐.
"""
n = int(input())

direction = list(map(str, input().split()))

x = 1
y = 1

for i in direction:
    if i == 'u' and x > 1:
        x -= 1
    if i == 'd' and x < n:
        x += 1
    if i == 'l' and y > 1:
        y -= 1
    if i == 'r' and y < n:
        y += 1

print(str(x) + ' ' + str(y))
