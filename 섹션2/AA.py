import sys
#sys.stdin = open('input.txt','rt')

''' 
숫자 n을 입력받아 k번째 약수를 구하는 문제
ex) n = 6 , k = 2
	n의 약수 1, 2, 3, 6 
	2번째 약수 = 2
'''

n, k = map(int, input().split()) # 입력이 띄어쓰기로 들어올 경우 map 사용 (줄바꿈x)
n_divisor = []


# 내가 짠 코드
for d in range(1, n+1):
	if n % d == 0:
		n_divisor.append(d)
if k>len(n_divisor):
	print(-1)
else:
	print(n_divisor[k-1])


# 강의 코드
'''
cnt = 0
for d in range(1, n+1):
	if n % d == 0:
		cnt +=1
	if cnt == k:
		print(d)
		break
else:
	print(-1)
'''