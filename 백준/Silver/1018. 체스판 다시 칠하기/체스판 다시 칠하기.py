pattern1 = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]
pattern2 = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

# 모든 가능한 8×8 부분 보드 확인하기
min_changes = float('inf')  # 최소값을 큰 값으로 초기화

# (i, j)가 8x8 보드의 시작 위치
for i in range(N - 7):
    for j in range(M - 7):
        changes1 = 0  # 패턴 1에서 다시 칠해야 하는 개수
        changes2 = 0  # 패턴 2에서 다시 칠해야 하는 개수

        # 8x8 보드 자르고 비교
        for x in range(8):
            for y in range(8):
                if arr[i + x][j + y] != pattern1[x][y]:
                    changes1 += 1  # 패턴 1과 비교해서 틀리면 다시 칠해야 하는 개수 증가
                if arr[i + x][j + y] != pattern2[x][y]:
                    changes2 += 1  # 패턴 2와 비교해서 틀리면 다시 칠해야 하는 개수 증가

        # 최소값 갱신
        min_changes = min(min_changes, changes1, changes2)

print(min_changes)

# 생각보다 어려워서 지피티의 도움을 좀 많이 받았다......