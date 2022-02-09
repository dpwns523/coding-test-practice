s, e = map(int, input().split()) 
ch = [0] * (e+1)
'''
에라토스테네스의 체 
2부터 시작해서 2, 3의 배수들을 모두 지워나감 -> 2의 배수들은 2를 제외한 수가 모두 소수가 아님
'''
for i in range(2, e+1):
    if ch[i] == 0:    # 소수
        if i >=s:
            print(i)
        for j in range(2*i, e+1, i):
            ch[j] = 1
           
