import math
# 낮에 a만큼 올라감 v만큼 가지못하면 b만큼 밤에 미끄러짐
a, b, v = map(int, input().split())
# 반복문을 통한 코드 -> 시간 초과
#loc = 0
#day = 0
#while True:
#    loc += a
#    if a>=v:
#        print(day+1)
#        break
#    else:
#        loc -= b
#        day += 1

# 마지막 정상에 오르기 전날까진 자는 것을 계산해야 함
print(math.ceil((v-a)/(a-b))+1)
