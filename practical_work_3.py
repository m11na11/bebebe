# Списки
# 1.
numbers = [10, 20, 30, 40, 50]
print('Первый элемент:', numbers[0])
print('Последний элемент:', numbers[-1])
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print('После обмена:', numbers)

# 2.
numbers = [10, 20, 30, 40, 50, 60]
middle = len(numbers) // 2
if len(numbers) % 2 == 1:
    print('Средний элемент:', numbers[middle])
else:
    print('Средние элементы:', numbers[middle - 1], numbers[middle])

# 3.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Первые три:', numbers[:3])
print('Последние три:', numbers[-3:])
print('Элементы с чётными индексами:', numbers[::2])
print('В обратном порядке:', numbers[::-1])

# 4.
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.insert(0, 5)
numbers.pop()
print(numbers)

# 5.
numbers = [10, 20, 30, 40, 50]
print('Длина:', len(numbers))
print('Сумма:', sum(numbers))
print('Минимум:', min(numbers))
print('Максимум:', max(numbers))
print('Среднее арифметическое:', sum(numbers) / len(numbers))

# 6.
numbers = [2, 5, 3, 5, 8, 5]
x = int(input('Введите число: '))
print('Есть в списке:', x in numbers)
print('Количество вхождений:', numbers.count(x))
if x in numbers:
    print('Индекс первого вхождения:', numbers.index(x))
else:
    print('Такого числа в списке нет')

# 7.
numbers = [12, 4, 25, 7, 1, 18, 9, 30]
sorted_numbers = sorted(numbers)
print('Три наименьших:', sorted_numbers[:3])
print('Три наибольших:', sorted_numbers[-3:])

# 8.
numbers1 = [3, 8, 1]
numbers2 = [5, 2, 9]
numbers = numbers1 + numbers2
numbers.sort(reverse=True)
print('Объединённый список:', numbers)
print('Второй по величине:', numbers[1])

# 9.
text = input('Введите слова через пробел: ')
words = text.split()
words.sort()
result = ', '.join(words)
print(result)

# 10.
numbers = [1, 2, 3, 4, 5]
k = int(input('Введите количество позиций: '))
k = k % len(numbers)
result = numbers[-k:] + numbers[:-k] if k != 0 else numbers.copy()
print('Результат:', result)


# Строки
# 1.
text = input('Введите строку: ')
print('Длина:', len(text))
print('Первый символ:', text[0])
print('Последний символ:', text[-1])

# 2.
text = input('Введите строку: ')
middle = len(text) // 2
if len(text) % 2 == 1:
    print('Средний символ:', text[middle])
else:
    print('Средние символы:', text[middle - 1], text[middle])

# 3.
text = input('Введите строку: ')
print('Первые три символа:', text[:3])
print('Последние три символа:', text[-3:])
print('Символы с чётными индексами:', text[::2])
print('В обратном порядке:', text[::-1])

# 4.
text = input('Введите строку: ')
print('Верхний регистр:', text.upper())
print('Нижний регистр:', text.lower())
print('С заглавной первой буквой:', text.capitalize())

# 5.
text = input('Введите строку: ')
c = input('Введите символ: ')
print('Есть в строке:', c in text)
print('Количество вхождений:', text.count(c))
if c in text:
    print('Индекс первого вхождения:', text.index(c))
else:
    print('Символ не найден')

# 6.
text = input('Введите строку: ')
text = text.replace(' ', '_')
print(text)

# 7.
text = input('Введите строку: ')
text = text.strip()
print('Результат:', text)
print('Длина:', len(text))

# 8.
text = input('Введите имя и фамилию: ')
name, surname = text.split()
print('Фамилия и имя:', surname, name)
print('Инициалы:', name[0] + '.' + surname[0] + '.')

# 9.
text = input('Введите строку: ')
text = text.lower()
if text == text[::-1]:
    print('Это палиндром')
else:
    print('Это не палиндром')

# 10.
text = input('Введите слова через пробел: ')
words = text.split()
print('Количество слов:', len(words))
print('Первое слово:', words[0])
print('Последнее слово:', words[-1])
