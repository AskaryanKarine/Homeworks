# Задание 3. Уровень - ресторатор.
# Условие: Вы стали успешным бизнесменом (потому что правильно подсчитали рентабельность в прошлом задании)
# и решили открыть свой ресторан  городе Круас-виль.
# Располагая капиталом, администрация ресторана решила оформить три 
# новых зала и закупить необходимое количество новых столов. За каждым столом может сидеть по два гостя. 
# Известно количество учащихся в каждом из трех классов. 
# Найдите наименьшее число столов, которое нужно приобрести для них.

# Входные данные: Программа получает на вход три натуральных числа: максимальное количество гостей в каждом из трех залов.

# Выходные данные: Ответ на задачу.

# Пример:
# Ввод                                                          Вывод
# 20
# 21
# 22                                                            32



a=[]
for i in range(3):
    a.append(int(input()))
print((sum(a)//2)+(sum(a)%2))