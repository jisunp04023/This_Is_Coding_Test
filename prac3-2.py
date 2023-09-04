# 실전 3-2
"""
여러 숫자 카드 중 높은 숫자가의 카드 한 장을 뽑는 게임.

게임의 룰
1. 숫자 카드는 n*m 형태로 놓여 있음 (n은 행의 개수, m은 열의 개수)
2. 행을 먼저 선택
3. 행에 포함된 카드 중 가장 낮은 숫자의 카드 뽑음
4. 행을 선택할 때, 행에서 가장 낮은 숫자 카드를 뽑을 것을 고려하여, 최종적으로 가장 높은 숫자 뽑을 수 있도록 전략.

첫째 줄에는 행의 개수 n과 열의 개수 m이 주어짐
둘째 줄부터 n개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐
"""

n, m = map(int, input().split())

candidate = []

for i in range(n):
    row = input().split()
    candidate.append(min(row))

print(max(candidate))
