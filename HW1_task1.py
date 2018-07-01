X = float(input('Длительность сна (в минутах):  '))
H = float(input('Время спать (часы):  '))
M = float(input('Время спать (минуты):  '))

H1 = H + (X // 60)
M1 = M + (X % 60)

print(H1)
print(M1)
