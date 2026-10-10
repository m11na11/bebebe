a = 10
b = 3.14
c = "Привет"
d = True
e = None

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

Age = 24
age = 15
print(Age)
print(age)#Age и age это две разные переменные из-за разного регистра букв 

print(int("1101", 2))
print(int("17", 8))
print(int("1F", 16))

num = 25
str_num = str(a)
float_num = float(a)
int_num = int(a)
print(str_num)
print(float_num)
print(int_num)

name = input('Введите имя:')
print('Привет,', name, '!')

a = int(input('Введите первое целое число:'))
b = int(input('Введите второе целое число:'))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = float(input('Введите длинну прямоугольника:'))
b = float(input('Введите ширину прямоугольника'))
print('Площадь прямоугольника:', a*b)
print('Периметр прямоугольника:', (a+b)*2)

year_birth = int(input('Введите год рождения'))
year_now = int(input('Введите текущий год'))
print('Ваш возраст:', year_now-year_birth)

a=int(input('Введите первое число:'))
b=int(input('Введите второе число:'))
a, b = b, a
print(a, b)

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = input('Введите знак операции (+, -, *, /):')
if c == '+':
    print('Ответ:', a + b)
elif c == '-':
    print('Ответ:', a - b)
elif c == '*':
    print('Ответ:', a * b)
elif c == '/':
    print('Ответ:', a/b)
else:
    print('Неизвестная операция')

sec = int(input('Введите количество секунд:'))
print(sec, '->', sec//3600, 'ч', (sec%3600)//60, 'мин', sec%60, 'сек')

sum = int(input('Введите сумму в рублях:'))
rub_in_usd = sum * 0.0119
rub_in_eur = sum * 0.0102
print('В долларах:', rub_in_usd)
print('В евро:', rub_in_eur)

r = int(input('Введите радиус круга:'))
print('Длина окружности:', 2 * 3.14 * r)
print('Площадь круга:', 3.14 * r ** 2)

name = str(input('Введите свое имя:'))
age = int(input('Введите свой возраст:'))
print(name,',', 'через 10 лет вам будет', age + 10, 'лет' )