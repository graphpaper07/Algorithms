a,b = map(int, input().split())
arr = [list(map(str, input())) for _ in range(a)]
total = 0

for i in range(a):
    temp = ''
    for j in range(b):
        if arr[i][j] == '-' and arr[i][j] != temp:
            total += 1
        temp = arr[i][j]

for j in range(b):
    temp = ''
    for i in range(a):
        if arr[i][j] == '|' and arr[i][j] != temp:
            total += 1
        temp = arr[i][j]

print(total)


