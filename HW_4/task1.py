n=int(input())
a=[]
res=[]
b=0
for i in range(n):
    m=int(input())
    for j in range(m):
        t,s=map(int, input().split())
        b+=s/t
    a.append(b)
    b=0
a.sort()
for x in a: print("{:.g}".format(x))