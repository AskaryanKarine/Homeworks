# Задание 5. Уровень - ну что за читер!?.
# Условие: Мария Ивановна выдала сложную контрольную по математике. Вы заметили, что 95% заданий - это вычисление
# производных от простейших функций (многочлены НЕ ВЫШЕ третьей степени). Пора дейстовать.

# Входные данные: Вводится натуральное число N - наибольшая степень анализируемого многочлена.
# Затем вводятся коэффициенты A,B,C,D,...Z многочлена вида : Ax^N + Bx^(N-1) + Cx^(N-2) + ... + Zx^(N-N) = 0
# В данной задаче число N не больше 3.

# Выходные данные : строка, явялющаяся аналитической формулой исследуемой производной.


# Пример:
# Ввод                                          Вывод
# 2
# 2 3 4                                         f(x)' = 4x + 3

# 1
# 5 7                                           f(x)' = 5

# 3
# 3 4 5 1                                       f(x)' = 9x^2 + 8x + 5

# В качестве ответа на данную задачу необходимо на проверку присылать файл, содержащий
# (обязательно) функцию find_der() ->str.
# В файле также могут содержаться дополнительные и вспоомогательные функции.
# Код, помещенный не в функции - в файле отсуствует.
def find_der() ->str:
    n = int(input())
    k = input().split()
    a = []
    res = "f(x)' = "
    for i in range(n+1): a.append(int(k[i]))
    a.reverse()
    for i in range(n, -1, -1):
        if i == 1:
            if a[i]>0: res += '+ '+str(a[i])
            else: res += '- '+ str(abs(a[i]))
        elif i == 2:
            if n == 2:
                res += str(a[i]*i)+'x ' 
            else:
                if a[i]>0: res += '+ '+str(a[i]*i)+'x '
                else: res += '- '+str(abs(a[i])*i)+'x '
        elif i == 3:
            res += str(a[i]*i)+'x^'+str(i-1)+' '
    return res
