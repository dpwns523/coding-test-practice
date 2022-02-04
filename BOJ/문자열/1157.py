# 문자열을 입력받고, 순회하면서 개수를 세면 된다.
a = input()
a = a.upper()
res = {}
# i에는 [M, S, S, ..]
for i in a:
    if i not in res.keys():
        res[i] =0
    res[i] +=1

max_val = max(res.values())
cnt = 0
tmp = ""
for k, v in res.items():
    if max_val == v:
        cnt += 1
        tmp = k
        
if cnt ==1:
    print(tmp)
else:
    print("?")
    
