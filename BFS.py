import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = []
visited = [-1] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while deque:
        now_node = queue.popleft()
        for i in A[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                queue.append(i)

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(x)

for i in range(N + 1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)

else:
    answer.sort()
    for i in answer:
        print(i)