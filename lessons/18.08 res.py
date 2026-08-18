a=input('Введите число: ')

flag=True

n=a[0]

if len(a)==1:
    print('YES')
else:
    for c in range(1,len(a)):
        if a[c]==n:
            continue
        else:
            flag=False
            break

    if flag:
        print('YES')
    else:
        print('NO')
