# 반복문을 통해 접근하면 시간초과
A, B, C = map(int, input().split())
if B >= C:
    print("-1")
else:
    # 한 개를 생산할 때마다 C-B의 차익이 생기며 고정비용 A만큼 이익을 내야함.
    # 손익분기점을 생각하여 +1을 한 만큼 생산해야함
    print(A//(C-B) + 1)
