# Задание 1. Уровень - лёгкая разминка.
# Условие: Юра любит бегать по утрам, поэтому он купил себе загадочное устройство "НИМБУС-РАНЕР-9000".
# После каждой пробежки устройство выдает Юре 2 числа --- время его пробежки (в минутах) , и отбеганное расстоение
# (в метрах). Юра хочет узнать свой прогресс в беге, поэтому ему срочно нужна программа - анализатор данных "НИМБУС-РАНЕРА-9000",
# которая будет высчитывать средний темп Юры на каждой пробежке, а затем выдавать их в порядке уменьшения среднего темпа.

# Входные данные: сначала вводится число N - количество анализируемых дней, затем для каждого дня вводится
# число M - количетсво пробежек в отдельно взятый день. После чего, для каждого дня вводят числа t и s (время и расстояние).

# Выходные данные: ежедневный средний темп (метры в минуту) в порядке уменьшения.

# Пример:
# Ввод:                                                                   Вывод:
# 2
# 1
# 20 2000
# 3
# 15 1500
# 30 6500
# 25 4200                                                                 161.5555
#                                                                         100




n=int(input())
a=[]
num=[]
b=0
for i in range(n):
    m=int(input())
    for j in range(m):
        t,s=map(int, input().split())
        b+=s/t
    a.append(b/m)
    b=0
a.sort()
for x in a: 
    k="{:.5f}".format(x)
    if k[-2]=='0' and k[-3]=='0' and k[-4]=='0' and k[-5]=='0': print(k[:k.find('.')])
    else: print(k[:k.find('.')+5])