import math
# 각 층의 맨 앞 호실부터 배정
c = int(input())
res = 0
for _ in range(c):
    h, w, n = map(int, input().split())
    res = math.ceil(n/h)    # 호실
    # 층
    if n%h == 0:        # 맨 꼭대기 층 배정
        res += 100*h
    else:    
        res += 100*(n%h)
    print(res)
