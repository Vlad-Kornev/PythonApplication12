# Программа находит наименьшее из списка чисел

mylist = [int(i) for i in input('Введите список чисел разделенных пробелом').split(' ')]
m = mylist[0]
for n in range(1,len(mylist)):
    if m >= mylist[n]:
        m = mylist[n]
        n +=1
    else:
        n +=1
print(str(m) + ' наименьшее число в списке')