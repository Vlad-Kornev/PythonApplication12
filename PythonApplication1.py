A = int(input('Введите число A: '))
B = int(input('Введите число В: '))
H = int(input('Введите число Н: '))

if (A <= H < B):
    print ('Это нормально')
elif (H < A):
    print ('Недосып')
else:
    print ('Пересып')