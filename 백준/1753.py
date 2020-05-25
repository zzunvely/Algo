import sys
from heapq import heappush, heappop #우선순위힙이용하기 위한 라이브러리
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(graph, start): #다익스트라 함수
    d = [inf for _ in range(v+1)]   #매 step마다 거리를 저장할 리스트
    d[start] = 0
    q = []
    heappush(q, [0, start])

    while q:  #큐에 원소가 없을때까지 반복
        cur_dis, cur_node = heappop(q)  #우선순위 큐에 의해 원소 출력
        if d[cur_node] < cur_dis:   #원소에 이미 저장되있는 거리가 현재 가중치보다 작은 경우 무시
            continue
        for node in graph[cur_node]:
            distance = cur_dis + node[1]  
            if distance < d[node[0]]:    #현재 경로와 저장된 경로비교 후, 최단경로 갱신
                d[node[0]] = distance
                heappush(q, [distance, node[0]])  #최단경로 갱신시, 우선순위 큐에 삽입
    return d

v, e = map(int, input().split())
k = int(input())
g = [[] for _ in range(v+1)]

for _ in range(e):   #그래프 입력, 초기화
    a, b, c = map(int, input().split())
    g[a].append([b, c])

for i in dijkstra(g, k)[1:]:  #다익스트라 함수 실행 및 결과 출력
    print(i if i != inf else "INF")
