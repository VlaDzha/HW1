s = input('Программисти:   ')
ns = float(s[-2:])
if ns >= 10 and ns <= 20:
    print(s, 'программистов')
else:
    if s[-1] == '1':
        print(s, 'прораммист')
    if s[-1] == '2' or s[-1] == '3' or s[-1] == '4': 
        print(s, 'програмиста')
    if s[-1] == '0' or s[-1] == '5' or s[-1] == '6' or s[-1] == '7' or s[-1] == '8' or s[-1] == '9':
        print(s, 'програмистов')