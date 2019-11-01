# Задание 2. Уровень - бизнесмен из школьной столовки.
# Условие: Вы - величайший предприниматель в школе №1.
# Именно Вы додумались покупать подешевке круассаны в магазине "Перекрестье" и продавать их в школе №1 на переменах.
# Главный вопрос, как подсчитать рентабельность вашего бизнеса? 


# Под рентабельностью будем понимать соотношение общей прибыли к выручке.
# Прибыль = выручка - издержки.
# Список ваших издержек : 
# Стоимость круассана --- 50 р.
# Разовая доставка неограниченного числа круассанов от дверей "Перекрестья" до школы №1 --- 500 р.
# Стоимость помощи бабки на входе с разгрузкой машины (за 1 коробку круассанов) --- 300 р.

# Принимая во внимание, что в 1 коробку влезает ровно 25 круассанов - ответьте на вопрос. Рентабельный ли ваш бизнес?

# Входные данные: сначала вводится натуральное число S --- стоимость Вашего круассана в школе №1, затем
# затем вводится число D (натуральное) - количество дней, за которое вы анализируете рентабельность, после
# чего вводится D раз два числа - A - количество купленных в "Перекрестье" круассанов и B - количество проданных в 
# в школе №1 круассанов.

# Выходные данные : "YES"  если рентабельность > 0.3 и "NO" в противном случае


# Пример:
# Ввод                                                                                    Вывод
# 100
# 2
# 200 200
# 350 250                                                                                "NO"

# 300
# 1
# 100 91                                                                                 "YES"




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