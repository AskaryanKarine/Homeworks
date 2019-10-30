s=int(input())
d=int(input())
gains=[]
revenues=[]
for i in range(d):
    a,b=map(int,input().split())
    if a%25!=0: cost=(a*50)+500+(((a//25)+1)*300)
    else: cost=(a*50)+500+((a//25)*300)
    revenue=b*s
    gain=revenue-cost
    gains.append(gain)
    revenues.append(revenue)
profitability=sum(gains)/sum(revenues)
if profitability>0.3: print('YES')
else: print('NO')