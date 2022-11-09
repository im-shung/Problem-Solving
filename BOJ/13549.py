# 0-1 BFS 알고리즘
# 개념: 가중치 0과 1로만 주어진 그래프에서 최단 경로를 찾는 알고리즘
# 시간복잡도: O(V+E)
# 동작방식
    # 1. deque.popleft()으로 정점 u을 꺼낸다
    # 2. 정점 u의 인접 정점을 체크한다.
    # 3. dist[u] + 간선(u,v)의 가중치 < dist[v] 인 경우 dist[v]를 갱신 (dist[i]: 시작점에서 i번 정점까지 가능한 최단 거리)
    # 4. 간선(u,v)의 가중치가 0이면 deque.appendleft(v), 1이면 deque.append(v)
    # 5. deque가 empty가 될 때까지 반복
# 요점! 가중치 0부터 처리한다

from _collections import deque

def bfs_0_1(dist, N, K):
    queue = deque()
    queue.append(N)
    dist[N] = 0

    while queue:
        x = queue.popleft()
        if x == K:
            return
        for dx in (x + 1, x - 1, x * 2):
            if 0 <= dx < 100_001 and dist[dx] == -1:
                if dx == x * 2:
                    queue.appendleft(dx)
                    dist[dx] = dist[x]
                else:
                    queue.append(dx)
                    dist[dx] = dist[x] + 1

if __name__ == '__main__':
    N, K = map(int, input().split())
    dist = [-1] * 100_001
    bfs_0_1(dist, N, K)
    print(dist[K])