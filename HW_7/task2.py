# Задача 1. Уровень - математик.
# Условие: Вам необходимо создать калькулятор обыкновенных дробей.
# Создайте класс Rational , который обладает следующими свойствами:
# 1) конструктор класса по умолчанию создает дробь вида 0 / 1
# 2) если у конструктора класса указано оба аргумента A и B (целые числа), то создается дробь вида A/B
# 3) если созданная дробь отрицательна - то минус ставится у числителя (-A/B)
# 4) если B = 0 - бросить исключение ZeroDivisionError и проинициализируйте дробь значением по умолчанию (0 / 1)
# 5)Создайте методы add(), sub(), div(), mult() для сложения, вычитания, умножения и деления дробей, резульатами всех
# этих операций должны быть НЕСОКРАТИМЫЕ ДРОБИ
# реализовать их можно в свободной форме. Пример реализации:
# a = Rational(1,2)
# b = Rational()
# c = a.add(b)
# d = a.sub(b)
# 6) создайте метод get() для вывода дроби в выходной поток . Выводить дробь надо в виде строки "A / B"


class Rational:

    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den
        try:
            self.intval = self.num/self.den
        except ZeroDivisionError as z_err:
            print(z_err)
            self.num = 0
            self.den = 1
        # формирование строки для вывода
        if self.den<0: 
            self.val = '-'+str(self.num)+' / '+str(abs(self.den))
        else: 
            self.val = str(self.num)+' / '+str(self.den)

    

    def add(self, fraction):
        nod = lambda f_num,s_num: f_num if s_num == 0 else nod(s_num, f_num % s_num) #лямбда-функция для НОД
        nok = lambda f_num,s_num: (f_num*s_num)/nod(f_num,s_num) # лямбда функция для НОК
        redn = lambda nums,dens: nums if nod(nums,dens)==1 else nums//nod(nums,dens) #лямба функция, которая сокращает числитель 
        redd =  lambda nums,dens: dens if nod(nums,dens)==1 else dens//nod(nums,dens) #лямбда функция, которая сокращает знаменатель
        #приведение к общему знаменателю
        k = int(nok(self.den, fraction.den)) 
        self.num = int(self.num*(k//self.den)) 
        second_num = int(fraction.num*(k//fraction.den))
        self.num = self.num+second_num
        # сокращение дроби
        second_num = redn(self.num, k)
        self.den = redd(self.num, k)
        # формирование строки для вывода
        if self.den<0: 
            self.val = '-'+str(second_num)+' / '+str(abs(self.den))
        else: 
            self.val = str(second_num)+' / '+str(self.den)
        

    def sub(self, fraction):
        nod = lambda f_num,s_num: f_num if s_num == 0 else nod(s_num, f_num % s_num) #лямбда функция нод
        nok = lambda f_num,s_num: (f_num*s_num)/nod(f_num,s_num) #лямбда функция нок
        redn = lambda nums,dens: nums if nod(nums,dens)==1 else nums//nod(nums,dens) # сокращение числителя
        redd =  lambda nums,dens: dens if nod(nums,dens)==1 else dens//nod(nums,dens) # сокращение знаменателя
        # приведение к общему знаменателю
        k = int(nok(self.den, fraction.den))
        self.num = int(self.num*(k//self.den)) 
        second_num = int(fraction.num*(k//fraction.den))
        self.num = self.num-second_num
        # сокращение дроби
        second_num = redn(self.num, k)
        self.den = redd(self.num, k)
        # формирование строки для вывода
        if self.den<0: 
            self.val = '-'+str(second_num)+' / '+str(abs(self.den))
        else: 
            self.val = str(second_num)+' / '+str(self.den)
        

    def mult(self, fraction):
        nod = lambda f_num,s_num: f_num if s_num == 0 else nod(s_num, f_num % s_num) #лямбда функция нод
        redn = lambda nums,dens: nums if nod(nums,dens)==1 else nums//nod(nums,dens) #сокращение числителя
        redd =  lambda nums,dens: dens if nod(nums,dens)==1 else dens//nod(nums,dens) #сокращение знаменателя
        # умножение дроби
        self.num = self.num * fraction.num
        self.den = self.den * fraction.den
        # сокращение дроби
        second_num = redn(self.num,self.den)
        self.den = redd(self.num, self.den)
        # формирование строки для вывода
        if self.den<0: 
            self.val = '-'+str(second_num)+' / '+str(abs(self.den))
        else: 
            self.val = str(second_num)+' / '+str(self.den)


    def div(self,fraction):
        nod = lambda f_num,s_num: f_num if s_num == 0 else nod(s_num, f_num % s_num) #лямбда функция нод
        redn = lambda nums,dens: nums if nod(nums,dens)==1 else nums//nod(nums,dens) #сокращение числителя
        redd =  lambda nums,dens: dens if nod(nums,dens)==1 else dens//nod(nums,dens) #сокращение знаменателя
        # деление доби
        self.num = self.num * fraction.den
        self.den = self.den * fraction.num
        # сокращение дроби
        second_num = redn(self.num,self.den)
        self.den = redd(self.num, self.den)
        # фомирование строки для вывода
        if self.den<0: 
            self.val = '-'+str(second_num)+' / '+str(abs(self.den))
        else: 
            self.val = str(second_num)+' / '+str(self.den)


    def get(self):
        # вывод ранее сформированной строки
        print(self.val)
