n=int(input('Сколько чисел вы хотите ввести: '))

m=0

napr=0 # переменная для направления

naprs=0 # переменная для старого направления

ma1=int(input('Введите первое число: ')) # назовем его мамкой 1

for i in range(1,n):

    mad=int(input('Введите новое число: ')) # здесь мы даем числа после первого

    if mad>ma1:
        napr=1
    elif mad==ma1:
        napr=0
    elif mad<ma1:
        napr=-1

    if napr!=0:
        if naprs==0:
            naprs=napr
        elif napr!=naprs:
            m+=1
            naprs=napr

    ma1=mad

print('Изменений направления: ',m)
