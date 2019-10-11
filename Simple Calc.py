a = float(input('введите число a'))
b = float(input('введите число b'))
c = input('введите арифметический опертор')
if c == '+':
    print(a + b)
elif c == '-':
    print (a - b)
elif (c == '/') and (b == 0.0):
    print ('Деление на 0!')
elif (c == '/') and (b != 0.0):
    print (a / b)
elif (c == '*'):
    print (a * b)
elif (c == 'mod') and (b == 0.0):
    print ('Деление на 0!')
elif (c == 'mod') and (b != 0.0):
    print (a % b)
elif (c == 'div') and (b == 0.0):
    print ('Деление на 0!')
elif (c == 'div') and (b != 0.0):
    print (a // b)
elif (c == 'pow'):
    print (a ** b)
else:
    print ('неизвестный арифметический оператор')