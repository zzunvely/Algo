import sys
input = sys.stdin.readline
inf = sys.maxsize

#입력받기, 그래프 초기화
n = int(input())
m = int(input())
g = [[inf]*(n+1) for i in range(n+1)]
f = []
for i in range(m):  #그래프 정보를 f에 저장한다
    f.append([int(x) for x in input().strip().split()])

start, end = map(int, input().strip())

touch = [0 for i in range(n+1)]
length = [0 for i in range(n+1)]

#처음 시작 노드를 제외한 모든 노드를 담은 line리스트
line = [i for i in range(1, n + 1) if (i != start)]
vnear = 0

for i in f:   # 입려받은 정보로, 그래프 갱시
    a, b, c = i[0], i[1], i[2]
    if g[a][b] > c:
        g[a][b] = c

for i in line:   #touch, length 초기화
    touch[i] = start
    length[i] = g[start][i]

for j in range(1, n):
    min = inf
    for i in line:   #length중 가장 작은 값을 min을 저장 및 vnear선택
        if (0 <= length[i]) and (length[i] < min):
            min = length[i]
            vnear = i

    if vnear == end or min == inf:  #vnear이 end값과 같으면 for문 종료
        break
    for l in line:   #vnear을 이용하여 length값 갱신 및 touch값 구하기
        if (length[vnear] + g[vnear][l]) < length[l]:
            length[l] = length[vnear] + g[vnear][l]
            touch[l] = vnear
    length[vnear] = -1 #선택된 노드는 -1로 갱신

final=0
while (end != start):  #touch를 통해 역추척하여 최단경로구하기
    final += g[touch[end]][end]
    end = touch[end]
print(final)