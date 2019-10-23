# Задание 3. Уровень - мастер пирамид из собак.

# Условие: На вход программе поступает натуральное число (A > 0) - высота пирамиды.
# Требуется вывести пирамиду из символов "@" указанной высоты.

# Входные данные : натуральное число A.
# Выходные данные: пирамида из символов "@" высоты A.


# Пример:
# Ввод:                                                    Вывод:
# 5                                                            @
#                                                             @@@
#                                                            @@@@@
#                                                           @@@@@@@
#                                                          @@@@@@@@@

n=int(input())
max_len=2*n-1
min_len=0
for i in range(n):
    min_len=2*i+1
    print(" "*((max_len-min_len)//2),"@"*min_len, sep="")
    