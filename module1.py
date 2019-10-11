y = int(input('Введите год: '))
if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 ==0) == False):
    print ('Обычный')
else:
    print ('Високосный')
