# Задание 4. Уровень - гросмейстер.
# Условие: Известно, что на доске 8×8 можно расставить 8 ферзей так, ч
# тобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга.

# Входные данные: программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.

# Выходные данные : eсли ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

# Пример:
# Ввод:                                        # Вывод:
# 1 7
# 2 4
# 4 8 
# 3 2
# 8 5
# 7 3
# 6 1 
# 5 6                                          NO

x=[]
y=[]
correct=True
for i in range(8):
    a,b=map(int, input().split())
    x.append(a)
    y.append(b)
for i in range(7):
    if x[i]==x[i+1] or y[i]==y[i+1] or abs(x[i]-x[i+1])==abs(y[i]-y[i+1]): correct=False
if correct:
    print("NO")
else:
    print("YES")
