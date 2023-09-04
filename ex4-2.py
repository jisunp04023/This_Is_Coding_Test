# 예제 4-2
"""
정수 n이 입력되면, 00시 00분 00초부터 n시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하라.

첫째 줄에 정수 n이 입력됨
"""
n = int(input())

cnt = 0

"""
풀이 1

for i in range(0, n + 1):
    if '3' in str(i):
        cnt += 60*60
    else:
        for j in range(0, 60):
            if '3' in str(j):
                cnt += 60
            else:
                for k in range(0, 60):
                    if '3' in str(k):
                        cnt += 1
"""

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
