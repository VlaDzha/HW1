t = input('Введите номер билета:    ')
if float(t[0]) + float(t[1]) + float(t[2]) == float(t[-1]) + float(t[-2]) + float(t[-3]):
    print('Счастливий!!!!!!')
else:
    print('Билет не счастливий... :( ')
