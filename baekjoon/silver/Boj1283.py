N = int(input())
short = set()
for _ in range(N):
    word = input()
    words = word.split()

    idx = -1
    for i in range(len(words)):
        if (words[i][0].upper() not in short):
            short.add(words[i][0].upper())
            idx = i
            break
    if idx != -1: # 단어의 첫 글자를 단축키로 지정할 수 있는 경우
        for i in range(len(words)):
            if idx == i:
                print("["+words[i][0]+"]"+words[i][1:], end=" ")
            else:
                print(words[i], end = " ")
        print()
    else:
        s = ""
        for w in word:
            if w != " " and w.upper() not in short:
                s = w
                short.add(w.upper())
                break

        if s != "":
            print(word.replace(s, "["+s+"]", 1))
        else:
            print(word)