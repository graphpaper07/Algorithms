BOARD_SIZE = 8
king, stone, N = input().split()
kingX, kingY = int(king[1]), ord(king[0]) - ord('A') + 1
stoneX, stoneY = int(stone[1]), ord(stone[0]) - ord('A') + 1
move = {"R": [0, 1],
        "L": [0, -1],
        "B": [-1, 0],
        "T": [1, 0],
        "RT": [1, 1],
        "LT": [1, -1],
        "RB": [-1, 1],
        "LB": [-1, -1]
        }
col = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}


def check_range(x, y):
    return x > 0 and y > 0 and x <= BOARD_SIZE and y <= BOARD_SIZE


for _ in range(int(N)):
    M = input()
    nx, ny = kingX + move[M][0], kingY + move[M][1]
    if (check_range(nx, ny)):
        if nx == stoneX and ny == stoneY:
            snx, sny = stoneX + move[M][0], stoneY + move[M][1]
            if (check_range(snx, sny)):
                kingX, kingY = nx, ny
                stoneX, stoneY = snx, sny
        else:
            kingX, kingY = nx, ny

print(col[kingY] + str(kingX))
print(col[stoneY] + str(stoneX))
