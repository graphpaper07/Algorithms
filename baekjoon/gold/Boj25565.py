N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def check_range(x, y):
    return x >= 0 and y >= 0 and x < N and y < M

row = set()
col = set()

def sumCol(i, j):
    ret = 0
    for _ in range(K):
        if check_range(i, j) and arr[i][j] == 1:
            ret += arr[i][j]
            i+=1
    return ret

for i in range(N):
    for j in range(M-K+1):
        if arr[i][j] == 1 and sum(arr[i][j:j+K]) == K:
            nx, ny = i, j
            while (check_range(nx, ny) and arr[nx][ny] == 1):
                row.add((nx, ny))
                ny+=1
            break


for j in range(M):
    for i in range(N-K+1):
        if arr[i][j] == 1 and sumCol(i, j) == K:
            nx, ny = i, j
            while (check_range(nx, ny) and arr[nx][ny] == 1):
                col.add((nx, ny))
                nx+=1
            break

intersection = row.intersection(col) # 교집합
if (len(intersection) == 1): # 교집합이 하나일 떄
    print(1)
    for elem in intersection:
        print(elem[0]+1, elem[1]+1)
elif (len(row) + len(col) == K * 2): # 교집합이 없을 때
    print(0)
else: # 교집합이 하나 이상일 때
    arr = list(row.union(col))
    arr.sort()
    arr = arr[len(arr)-K:K]
    print(len(arr))
    for elem in arr:
        print(elem[0]+1, elem[1]+1)
