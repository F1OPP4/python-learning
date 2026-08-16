# Изучение Python — урок 01
# Темы: for/range, if/elif/else, break, continue,
# вложенные циклы, строки, индексы, срезы и методы строк.

# 1. range + if + break/continue
for i in range(1, 21):
    if i % 3 == 0:
        if i % 5 == 0:
            break
        else:
            print(i)

# 2. break перед следующим условием
for i in range(1, 31):
    if i == 25:
        break
    elif i % 3 == 0:
        if i % 5 == 0:
            continue
        else:
            print(i)

# 3. Вложенные циклы
for i in range(3):
    for a in range(3):
        print(i, a)

# 4. Простой квадрат из символов с помощью вложенных циклов
for i in range(4):
    for a in range(4):
        print('*', end=' ')
    print()

# 5. Строки: перебираем символы строки по очереди
word = 'libertea'
for letter in word:
    print(letter)

# 6. Индексы и срезы
word = 'libertea'
print(word[0:5])
print(word[3:7])
print(word[::2])
print(word[::-1])
print(word[::-2])

# 7. Проверяем, является ли слово палиндромом
word = input('Введите слово: ')
word = word.replace(' ', '')

if word.lower() == word.lower()[::-1]:
    print('Палиндром')
else:
    print('Обычное слово')

# 8. Методы строк
word = input('Введите слово: ')
print('Длина:', len(word))
print('Заглавными буквами:', word.upper())

# 9. Считаем количество определённого символа
word = input('Введите строку: ').lower()
count = 0

for letter in word:
    if letter == 'a':
        count += 1

print('a =', count)

# 10. Считаем гласные и согласные
word = input('Введите строку: ').lower()
consonants = 0
vowels = 0

for letter in word:
    if letter.isalpha():
        if letter in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print('Гласных:', vowels)
print('Согласных:', consonants)

# 11. Считаем буквы, цифры, гласные и согласные
word = input('Введите строку: ').lower()
letters = 0
digits = 0
vowels = 0
consonants = 0

for letter in word:
    if letter.isalpha():
        letters += 1

        if letter in 'aeiou':
            vowels += 1
        else:
            consonants += 1

    elif letter.isdigit():
        digits += 1

print('Букв:', letters)
print('Цифр:', digits)
print('Гласных:', vowels)
print('Согласных:', consonants)
