import csv

def add_expence(slov, cat, amount):
    if cat in slov:
        slov[cat] += amount
    else:
        slov[cat] = amount


sumka = {}
daily = {}
summa = 0
max_amount = 0
max_description = ''
max_date = ''

with open("expences.csv", "r", encoding="utf-8") as expences:
    reader = csv.reader(expences)
    next(reader)

    for row in reader:
        date, category, amount, description = row
        amount = int(amount)

        # Расходы по категориям
        add_expence(sumka, category, amount)

        # Расходы по дням
        add_expence(daily, date, amount)

        # Общая сумма
        summa += amount

        # Самая большая отдельная покупка
        if amount > max_amount:
            max_amount = amount
            max_description = description
            max_date = date

# Самый дорогой день
max_d_amount = 0
max_d_date = ''

for date, amount in daily.items():
    if max_d_amount < amount:
        max_d_amount = amount
        max_d_date = date

print(f'По категориям: {sumka}')
print(f'Всего: {summa}')
print(f'Самая большая покупка: {max_description} - {max_amount} ₽, дата: {max_date}')
print(f'Самый дорогой день: {max_d_date} — {max_d_amount} ₽')
