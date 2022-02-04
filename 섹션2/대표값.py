import sys
# sys.stdin = open('input.txt','rt')

'''
대표값
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.
▣ 입력예제 1
10
45 73 66 87 92 67 75 79 75 80
▣ 출력예제 1
74 7
예제설명
평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다. 여기서 점수가 높은
75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.
'''

# 아이디어. 입력을 다받고, 평균을 구함-> 1단계
# 2단계 -> 평균과 가장 가까운 점수들의 리스트를 만들고 그중 가장 큰값을 구함
# 3단계 -> 같은값의 리스트 인덱스를 찾아 출력

n = int(input())
a = list(map(int, input().split()))

arrMin = float('inf')

mean = round(sum(a)/n) # 소수점 첫째자리에서 반올림 #에러 0.5에서 반올림하면 0임
#mean = round(mean)
ans = 0
idx = 0
for i in range(n): #평균과 차이가 제일 적은 값을 찾는다.
    if abs(a[i]-mean) < arrMin:
        arrMin = abs(a[i]-mean)
        ans=a[i]
        idx = i
    elif abs(a[i]-mean) == arrMin:
        if ans < a[i]:      # ans와 a[i]가 같은 값일 경우 자동적으로 인덱스가 작은게 저장됨 순차접근.
            ans = a[i]
            idx = i
print('%d %d' %(mean, idx+1))
# 강의 코드
'''
min = 'inf'
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1

    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print('%d %d' %(mean, res))
'''
