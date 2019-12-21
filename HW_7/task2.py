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
        self.val = str(abs(self.num))+' / '+str(abs(self.den))
        if self.den*self.num<0: 
            self.val='-'+self.val
    
    def reduction(self):
        nod = lambda f_num,s_num: f_num if s_num == 0 else nod(s_num, f_num % s_num) #лямбда-функция для НОД
        redn = lambda nums,dens: nums if nod(nums,dens)==1 else nums//nod(nums,dens) #лямба функция, которая сокращает числитель 
        redd =  lambda nums,dens: dens if nod(nums,dens)==1 else dens//nod(nums,dens) #лямбда функция, которая сокращает знаменатель
        k = self.num
        self.num = redn(k,self.den)
        self.den = redd(k,self.den)
        self.val = str(abs(self.num))+' / '+str(abs(self.den))
        if self.den*self.num<0: 
            self.val='-'+self.val


    def add(self, fraction):
        self.num = (self.num * fraction.den) + (fraction.num * self.den)
        self.den = self.den * fraction.den
        self.reduction()

    def sub(self, fraction):
        self.num = self.num*fraction.den - fraction.num*self.den
        self.den = self.den*fraction.den
        self.reduction()


    def mult(self, fraction):
        self.num = self.num * fraction.num
        self.den = self.den * fraction.den
        self.reduction()

    def div(self,fraction):
        self.num = self.num * fraction.den
        self.den = self.den * fraction.num
        self.reduction()

    def get(self):
        print(self.val)