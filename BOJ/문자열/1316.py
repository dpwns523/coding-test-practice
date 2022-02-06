# 입력받은 문자열을 순차접근하여 앞 뒤 문자가 다를 시 현재 문자가 뒤에 나타나면 그룹단어가 아님

cnt = int(input())
res = cnt
for _ in range(cnt):
    s = input()
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i] in s[i+1:]:
                res -= 1
                break
print(res)
