# 실전 4-2
"""
게임 캐릭터는 n*m 크기의 직사각형에서 움직이며 각각의 칸은 육지 또는 바다이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (a, b). a는 북쪽으로부터 떨어진 칸의 개수, b는 서쪽으로부터 떨어진 칸의 개수.
캐릭터는 상하좌우로 움직일 수 있고, 바다는 갈 수 없음.

1. 현재 방향을 기준으로 왼쪽 방향부터 반시계방향으로 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면,
    왼쪽으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
    왼쪽 방향에 가보지 않은 칸이 없다면,
    왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향이 모두 이미 방문한 칸이거나 바다인 경우,
    바라보는 방향을 유지한 채 한 칸 뒤로가고 1단계로 돌아간다.
    뒤쪽 칸이 바다라서 이동 불가한 경우 움직임을 종료한다.

캐릭터가 방문한 칸의 수를 출력하라.

첫째 줄에 맵의 세로크기 n과 가로크기 m을 입력.
둘째 줄에 캐릭터가 있는 좌표 (a, b)와 바라보는 방향 d가 주어짐.
d는 0(북), 1(동), 2(남), 3(서) 값을 가짐.
셋째 줄부터 맵이 육지인지 바다인지 정보 주어짐 0(육지), 1(바다).
"""

n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 북, 동, 남, 서 방향을 각각 0, 1, 2, 3 인덱스에 저장
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

array = [] # 맵 정보
track = [] # 방문 기록을 할 비어있는 맵 생성

for i in range(n):
    array.append(list(map(int, input().split())))
    track.append([0] * m)

track[x][y] = 1 # 시작 위치를 방문으로 체크


# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


# 시뮬레이션 시작
cnt = 1 # 방문한 칸의 개수 (시작 위치를 방문했으니 1로 초기화)
turn_cnt = 0 # 회전 수

while True:
    turn_left() # 왼회전
    # 왼쪽 좌표 구하기 (다음 이동할 후보 좌표 구해두기)
    next_x = x + dx[d]
    next_y = y + dy[d]

    if track[next_x][next_y] == 0 and array[next_x][next_y] == 0: # 방문한적x, 육지o
        track[next_x][next_y] = 1 # 방문처리
        cnt += 1
        x = next_x # 방문좌표로 이동
        y = next_y
        turn_cnt = 0

    else: # 방문 불가한 경우
        turn_cnt += 1 # 왼쪽으로 한번 돌았음을 체크

    if turn_cnt == 4: # 네 방향 모두 방문했거나, 바다인 경우
        # 뒷쪽 좌표 구하기 (다음 이동할 후보 좌표 구해두기)
        next_x = x - dx[d]
        next_y = y - dy[d]

        if array[next_x][next_y] == 0: # 뒷칸이 육지인 경우
            x = next_x  # 방문좌표로 이동
            y = next_y
            turn_cnt = 0

        else: # 뒷칸이 바다인 경우
            break

print(cnt)


