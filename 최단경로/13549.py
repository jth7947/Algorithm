import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([(n, 0)])
visited = [-1 for _ in range(100001)]
visited[n] = 0
count = 0
while n != k:
    n, count = queue.popleft()
    count += 1
    if n * 2 <= 100000 and visited[n * 2] == -1:
        visited[n * 2] = count - 1
        queue.appendleft((n * 2, count - 1))
    if n - 1 >= 0 and visited[n - 1] == -1:
        visited[n - 1] = count
        queue.append((n - 1, count))
    if n + 1 <= 100000 and visited[n + 1] == -1:
        visited[n + 1] = count
        queue.append((n + 1, count))


print(visited[k])