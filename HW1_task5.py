D = float(input("Введите растояние между домами:  "))
P = float(input("Введите цену кабеля:  "))
i = 1
L = 0
for i in 1, 2, 3, 4, 5:
    for j in range(i + 1, 7):
        L = L + (j - i) * D
#        print('i=', i, 'j=', j, 'L=', L)
print('Длинна кабеля:  ', L )
print('Стоимость кабеля:  ', L * P  )
