s = int(input())
e = int(input())
res = 0
if s == 1:    # 1은 소수가 아니므로 제외
    s=2
flag = False
minx = 21470000
for i in range(s, e+1):
    for j in range(2, i):
        if i % j == 0:    # 소수가 아니다
            flag = True
            break
    if flag:
        flag = False
    else:
        if minx > i:
            minx = i
        res += i
if res == 0:
    print(-1)
else:
    print(res)
    print(minx)
