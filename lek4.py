
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("\nВыберите операцию:")
print("1. +  Сложение")
print("2. -  Вычитание")
print("3. *  Умножение")
print("4. /  Деление")
print("5. // Целочисленное деление")
print("6. %  Остаток от деления")
print("7. ** Возведение в степень")
print("8. Сравнение чисел")
print("9. Логические операции")
print("10. Проверка принадлежности")
print("11. Проверка тождественности")

operation = input("Введите номер операции: ")

if operation == "1":
        print("Результат:", a + b)

elif operation == "2":
        print("Результат:", a - b)

elif operation == "3":
        print("Результат:", a * b)

elif operation == "4":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("Ошибка: деление на ноль!")

elif operation == "5":
        if b != 0:
            print("Результат:", a // b)
        else:
            print("Ошибка: деление на ноль!")

elif operation == "6":
        if b != 0:
            print("Результат:", a % b)
        else:
            print("Ошибка: деление на ноль!")

elif operation == "7":
        print("Результат:", a ** b)

elif operation == "8":
        print("Равно:", a == b)
        print("Не равно:", a != b)
        print("Первое больше:", a > b)
        print("Первое меньше:", a < b)
        print("Первое больше или равно:", a >= b)
        print("Первое меньше или равно:", a <= b)

elif operation == "9":
        print("Оба числа положительные:", a > 0 and b > 0)
        print("Хотя бы одно число положительное:", a > 0 or b > 0)
        print("Первое число не положительное:", not (a > 0))

elif operation == "10":
        numbers = [a, b]
        print("Число a есть в списке:", a in numbers)
        print("Число 0 отсутствует в списке:", 0 not in numbers)

elif operation == "11":
        x = a
        y = a
        z = b

        print("x is y:", x is y)
        print("x is not z:", x is not z)

else:
        print("Ошибка: такой операции нет!")
