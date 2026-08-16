# Python learning — Lesson 01
# Topics: for/range, if/elif/else, break, continue,
# nested loops, strings, indexing, slicing and string methods.

# 1. range + if + break/continue
for i in range(1, 21):
    if i % 3 == 0:
        if i % 5 == 0:
            break
        else:
            print(i)

# 2. break before another condition
for i in range(1, 31):
    if i == 25:
        break
    elif i % 3 == 0:
        if i % 5 == 0:
            continue
        else:
            print(i)

# 3. Nested loops
for i in range(3):
    for a in range(3):
        print(i, a)

# 4. A simple square made with nested loops
for i in range(4):
    for a in range(4):
        print('*', end=' ')
    print()

# 5. Strings: iterate through characters
word = 'libertea'
for letter in word:
    print(letter)

# 6. Indexing and slicing
word = 'libertea'
print(word[0:5])
print(word[3:7])
print(word[::2])
print(word[::-1])
print(word[::-2])

# 7. Palindrome
word = input('Enter a word: ')
word = word.replace(' ', '')

if word.lower() == word.lower()[::-1]:
    print('Палиндром')
else:
    print('Обычное слово')

# 8. String methods
word = input('Enter a word: ')
print('Length:', len(word))
print('Uppercase:', word.upper())

# 9. Count a character
word = input('Enter a string: ').lower()
count = 0

for letter in word:
    if letter == 'a':
        count += 1

print('a =', count)

# 10. Count vowels and consonants
word = input('Enter a string: ').lower()
consonants = 0
vowels = 0

for letter in word:
    if letter.isalpha():
        if letter in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print('Vowels:', vowels)
print('Consonants:', consonants)

# 11. Count letters, digits, vowels and consonants
word = input('Enter a string: ').lower()
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

print('Letters:', letters)
print('Digits:', digits)
print('Vowels:', vowels)
print('Consonants:', consonants)
