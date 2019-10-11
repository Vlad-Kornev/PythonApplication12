# Сумма целых чисел от a до b
a = int(input('введите число a'))
b = int(input('введите число b'))
if b <= a:
    print('введите число b еще раз, b должно быть больше a')
    b = int(input())
else:
    s = 0
    i = a
    while i <= b:
        s += i 
        i += 1
        
print ('сумма простых чисел от a до b равна', s)
