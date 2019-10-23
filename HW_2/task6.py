# Задание 6. Уровень - Кодзима, ты ли это?
# Условие: вы создали игру в жанре шутер. Теперь ваш дизайнер придумал новое неизвестное никому оружее - дробовик.
# Известно, что дробовики стреляют дробью (внезапно, правда?). Ваша задача - рассчитать суммарный урон, наненсенный 
# выстрелом из дробовика.


# Входные данные : Сначала вводится количество дробинок.
# Затем урон от каждой дробинки. Урон от каждой дробинки выражается простой дробью, 
# её числитель и знаменатель вводятся на отдельных строках.

# Выходные данные : Суммарный урон, выраженный простой несократимой дробью с дробной 
# чертой между числителем и знаменателем.


# Пример:
# Ввод:                                               # Вывод:
# 2
# 1
# 50
# 3
# 20                                                 17/100


# 3
# 1
# 50
# 2
# 40
# 3 
# 30                                                 17/100


#ФУНКЦИИ

def NOD(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else: 
            b=b-a
    return a

def NOK(a,b):
    return (a*b)/NOD(a,b)

def reduction(a,b):
    k=NOD(a,b)
    if k==1: s=str(a)+'/'+str(b)
    else:
        a=a//k
        b=b//k
        s=str(a)+'/'+str(b)
    return s

#ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ

n=int(input())
nums=[]
dens=[]
num=0
den=0

#ЧТЕНИЕ ДАННЫХ

for i in range(n):
    a=int(input())
    b=int(input())
    nums.append(a)
    dens.append(b)

if n==0: print(0)
elif n==1:
    print(reduction(nums[0],dens[0]))
elif n==2:
     k=int(NOK(dens[0],dens[1]))
     nums[0]=int(nums[0]*(k//dens[0]))
     nums[1]=int(nums[1]*(k//dens[1]))
     num=nums[0]+nums[1]
     print(reduction(num,k))
else:
    k=NOK(dens[0],dens[1])
    for i in range(2, n): k=int(NOK(k,dens[i]))
    for i in range(n): nums[i]=int(nums[i]*(k//dens[i]))
    num=sum(nums)
    print(reduction(num,k))      
