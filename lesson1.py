print ("Hello world") # функция вывода
print('Hello', "World") #

message = "Hello" #вывод с помощью переменной, имя переменной (как правило) должно начинаться с маленькой буквы
print(message)   # переменная - это ссылка на какой-то объект в pycharm
# переменная всегда в нижнем регистре
# для имени переменной нельзя использовать зарезервированные под команды слова( print)


#                Как лучше ,как надо

# my_text = 'Какой-то текст'
# first_name = "Oksana"
# counter = 0
# price = 100
#                      КАК НЕ НАДО
# myText = "Какой-то текст"
# FirstName = "Oksana"
# счетчик = 0
# mdfgdfbf = 100
# print = "Hello" (функция print)

# ОСНОВНЫЕ ТИПЫ

# строка (str) "Hello"
# числа (number) 100
# вещ. числа (float) 3.14
# булево  FALSE\TRUE
# None ничего (у = None)
# Язык динамически типизированнфый язык - типы данных можно менять в ходе процесса проги

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ С ЧИСЛАМИ (ОПЕРАТОРЫ)

# +,  -,  /, * ------  сложение, вычитание, деление, умножение
#  // целочисленное деление  (10 // 3 = 3)
#  %  Остаток от деления ( 10 % 3 = 1)

a = 100
b = 200
result = a + b
print(result)

a = 100 + 2
b = 80 - 45
c = 45 / 2
d = 100 // 30
e = 4*3
f = 10%3
print(a, b, c, d, e, f)


#string = "100" # это не число а просто текст и нельзя совершать операции

#                   ПРЕОБРАЗОВАНИЕ ТИПОВ
'''
# str() преобразует  число в строку  ----  str(100) --> "100"
# int() преобразует строку в число ------ int("100") --> 100
# a = "100"
# b = 200
# result = int(a) + b
# print(result)

# num = 100
# str_num = str(num)  # "100"
# print(str_num + "mm")

# Функция ввода данных input
'''
'''
# message = input("Введите ваше сообщение: ")
# print(message)
# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# result = a + b
# print(result)
#
# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# result = int(a) + int(b)
# print(result)
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# result = a + b
# print(result)
'''

name = input()
surname = input()
fullname = name + surname  # ИванИванов
print("Привет, меня зовут:", fullname)

name = input()
surname = input()
fullname = name + " " + surname #конкатенация  (добавили пробел) --> Иван Иванов
print("Привет, меня зовут:", fullname)


name = input()
surname = input()
fullname = name + surname  # ИванИванов
print(f"Привет, меня зовут:, {name} {surname} !")
'''   f - это функция, в которой можно динамически 
      # подставить значения из переменных   более предпочтительный
'''
a = 100
b = 34
result = a + b
print(f"{a} + {b} = {result}")
print(f"{{a}} + {{b}} = {result}") # --> Экранирование фиг скобок, выведет числа в фиг скобках

 #                 МЕТОДЫ strok


# .lower()
# .upper()
# .title() # переводит КАЖДУЮ ПЕРВУЮ букву слова в верхний регистр, остальные в нижний (Меня Зовут Слава)
# .capitalize()  # переводит первую букву строки в верхний регистр, остальные в нижний( Меня зовут слава)

string = "Hello world"
lower_string = string.lower() # все буквы в строке переводит в нижний регистр
lower_string = string.upper()  # все буквы переводит в верхний регистр --> HELLO WORLD
print(lower_string) # --> hello world

name = input() #ИВАН  Можно сразу в начале приписать метод: name = input().title().upper()
surname = input() #иВанов

print(f"Привет, меня зовут:, {name.title()} {surname.title()} !")  #--> Иван Иванов

