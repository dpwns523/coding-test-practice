import math
c = int(input())
for _ in range(c):
    x, y = map(int, input().split())
    distance = y - x
    # 1 -> 1 = 1
    # 2 -> 1 1 = 2
    # 3 -> 1 1 1 = 3
    # 4 -> 1 2 1 = 3
    # 5 -> 1 2 1 1 = 4
    # 6 -> 1 2 2 1 = 4
    # 7 -> 1 2 2 1 1 = 5
    # 8 -> 1 2 2 2 1 = 5
    # 9 -> 1 2 3 2 1 = 5
    # 10 -> 1 2 3 2 1 1 = 6
    n = (int)(math.sqrt(distance))
    tmp = (int)(math.pow(n, 2))
    if distance == tmp:
        print((2*n)-1)
    elif tmp < distance <= tmp+n:
        print(2*n)
    else:
        print((2*n)+1)
