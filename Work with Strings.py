n = input('Укажите число программистов зафиксированное роботом')

# Далее идет работа со срезами, обычно обозначение среза имеет вид: n[a:b], где а и b являются индексами первого и последнего символов среза, при этом 
# последний символ не включается в срез, если его необходимо включить (например в конце строки) то значение индекса последнего символа среза не заполняется,
# например срез из последнегл символа строки можно записать вот так: n[-1:]

if (int(n[-1:]) == 0) or (5 <= int(n[-2:]) <= 19) or (int(n[-1:]) == 5) or (int(n[-1:]) == 6) or (int(n[-1:]) == 7) or (int(n[-1:]) == 8) or (int(n[-1:]) == 9):
    print (n + ' ' + 'программистов')
elif (int(n[-1:]) == 1):
    print (n + ' ' + 'программист')
elif (2 <= int(n[-2:]) <= 4) or (int(n[-1:]) == 2) or (int(n[-1:]) == 3) or (int(n[-1:]) == 4):
    print (n + ' ' + 'программиста')