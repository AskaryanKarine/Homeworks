n=int(input())
s1=[]
res=[]
for i in range(n): res.append(False)
for i in range(n):
    s=input().lower()
    for j in range(len(s)):
        if (s[j]>='a' and s[j]<='z') or (s[j]>='0' and s[j]<='9') or (s[j]>='а' and s[j]<='я'): s1.append(s[j])    
    k=len(s1)
    for j in range(len(s1)//2):
        if s1[j]!=s1[k-j-1]:
            #print(s1[j], s1[k-j-1])
            res[i]=True
            break 
    s1=[]
for i in range(n):
    if res[i]:
        if i%2==0:
            print('Сослан на Плутон Юра')
            break
        else:
            print('Сослан на Плутон собеседник')
            break
if sum(res)==0: print('Сослать обоих')