"""문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다."""

import sys
input = sys.stdin.readline
INF = float("inf")
n, e = list(map(int, input().split()))
board = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(e):
    a, b, c = list(map(int, input().split()))
    board[a][b] = min(board[a][b], c)
    board[b][a] = board[a][b]

for i in range(n + 1):
    board[i][i] = 0

v1, v2 = map(int, input().split())
distance1 = [INF for _ in range(n + 1)]
distance2 = [INF for _ in range(n + 1)]
distance1[v1] = 0
distance2[v2] = 0
visited1 = [False for _ in range(n + 1)]
visited2 = [False for _ in range(n + 1)]

index1 = v1
for i in range(n):
    distance = INF
    for j in range(1, n + 1):
        if distance1[j] < distance and not visited1[j]:
            index1 = j
            distance = distance1[j]
    if distance == INF:
        break

    visited1[index1] = True
    for k in range(1, n + 1):
        if board[index1][k] != INF and not visited1[k]:
            distance1[k] = min(distance1[k], distance1[index1] + board[index1][k])


index2 = v2
for i in range(n):
    distance = INF
    for j in range(1, n + 1):
        if distance2[j] < distance and not visited2[j]:
            index2 = j
            distance = distance2[j]
    if distance == INF:
        break

    visited2[index2] = True
    for k in range(1, n + 1):
        if board[index2][k] != INF and not visited2[k]:
            distance2[k] = min(distance2[k], distance2[index2] + board[index2][k])

distance = min(distance1[1] + distance1[v2] + distance2[n], distance1[n] + distance1[v2] + distance2[1])
if distance == INF:
    print(-1)
else:
    print(distance)