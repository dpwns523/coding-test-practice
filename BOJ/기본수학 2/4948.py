# 에라토스테네스의 체 이용

while True:
    n = int(input())
    if n == 0:
        break
    ch = [0]*((2*n)+1)
    cnt = 0
    for i in range(2, (2*n)+1):
        if ch[i] == 0:
            if i > n:
                cnt += 1
            for j in range(i, (2*n)+1, i):
                ch[j] = 1
    print(cnt)
        
