a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
last_result = None

print('Выберите операцию:')
print('1. +  Сложение')
print('2. -  Вычитание')
print('3. *  Умножение')
print('4. /  Деление')
print('5. // Целочисленное деление')
print('6. %  Остаток от деления')
print('7. ** Возведение в степень')
print('8. Сравнение чисел')
print('9. Проверка равенства нулю')
print('10. Проверка наличия цифры в числе')
print('11. Проверка сохранённого результата')

operation = input('Введите номер операции: ')

if operation == '1':
        last_result = a + b
        print('Результат:', last_result)

elif operation == '2':
        last_result = a - b
        print('Результат:', last_result)

elif operation == '3':
        last_result = a * b
        print('Результат:', last_result)

elif operation == '4':
        if b != 0:
                last_result = a / b
                print('Результат:', last_result)
        else:
                print('Ошибка: делить на ноль нельзя!')

elif operation == '5':
        if b != 0:
                last_result = a // b
                print('Результат:', last_result)
        else:
                print('Ошибка: делить на ноль нельзя!')

elif operation == '6':
        if b != 0:
                last_result = a % b
                print('Результат:', last_result)
        else:
                print('Ошибка: делить на ноль нельзя!')

elif operation == '7':
        last_result = a ** b
        print('Результат:', last_result)

elif operation == '8':
        last_result = print(f'Равно: {a == b}\nНе равно: {a != b}\nПервое больше: {a > b}\nПервое меньше: {a < b}\nПервое больше или равно: {a >= b}\nПервое меньше или равно: {a <= b}')

elif operation == '9':
        if a == 0 and b == 0:
                print('Оба числа равны нулю')
        elif (a == 0 and b != 0) or (a != 0 and b == 0):
                print('Только одно число равно нулю')
        elif not (a == 0 or b == 0):
                print('Ни одно число не равно нулю')   

elif operation == '10':
        digit = input("Введите цифру для поиска: ")
        if digit not in '0123456789' or len(digit) != 1:
                print('Ошибка: введите одну цифру от 0 до 9!')
        elif digit in str(a) and digit not in str(b):
                print("Цифра есть в первом числе")
        elif digit in str(b) and digit not in str(a):
                print("Цифра есть во втором числе")
        elif digit in str(a) and digit in str(b):
                print("Цифра есть в обоих числах")
        else:
                print("Цифра не найдена в обоих числах")
elif operation == '11':
    if last_result is None:
        print('Сохранённого результата нет')
    elif last_result is not None:
        print('Сохранённый результат:', last_result)

else:
        print('Ошибка: такой операции нет!')
