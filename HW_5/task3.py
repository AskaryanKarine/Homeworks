# Задание 3. Уровень - сильный дерзкий.

# Условие: напишите программу, которая для данного текста подсчитывает частоты всех буквенных символов в нем. 
# Пунктуацию учитывать не нужно.
# Регистр не важен. То есть символы 'А' и 'а' - эквивалентны.



# Входные данные: произвольный текст.

# Выходные данные: таблица с частотами символов. 
# Таблица должна быть отсортирована по убыванию частот, в случае равных частот — в алфавитном порядке. 
# Если в тексте нет алфавитных символов - выводим перенос строки.

# Пример:
# Ввод:                                      # Вывод:
# hello, world!                              l: 3
#                                            o: 2
#                                            d: 1
#                                            e: 1
#                                            h: 1
#                                            r: 1
#                                            w: 1

# В качестве ответа на данную задачу необходимо на проверку присылать файл, содержащий
# (обязательно) функцию counted_str(message: str) -> dict.
# В файле также могут содержаться дополнительные и вспоомогательные функции.
# Код, помещенный не в функции - в файле отсуствует.


def counting(s:str) -> dict:
    s = s.lower()
    s1 = ''
    a = {}
    for i in range(len(s)):
        if s[i].isalpha(): s1 += s[i]
    for i in range(len(s1)):
        if s1[i] not in a.keys():
            a[s1[i]]=1
        else:
            a[s1[i]]+=1
    return a

def counted_str(message: str) -> dict:
    res = {}
    message = message.lower()
    if len(message) == 0:
        res.update('\n')
    d = counting(message)
    c = list(d.items())
    c.sort(reverse=True, key=lambda i: i[1])
    d = {}
    for v,k in c:
        if k not in d.keys():
            d.update({k:v})
        else:
            d[k] += v
    for k,v in d.items():
        if len(v) == 1:
            res.update({v:k})
            # print(v, ': ', k, sep='')
        else:
            c = list(d[k])
            c.sort()
            for x in c:
                res.update({x:k})
                # print(x, ': ', k, sep='')
    return res
