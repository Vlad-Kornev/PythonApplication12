# Программа считывает список чисел из первой строки и число из второй, а затем выводит по возрастанию индексы всех элементов списка, равных данному числу.



mlist = [int(i) for i in input().split()]
k = int(input())
mstring = ''
if mlist.count(k) == 0: # проверка списка на предмет наличия элементов, равных заданному числу
    print ('Отсутствует')
else:
    for i in range(0,len(mlist)): # поочередное сравнение элементов списка с заданным числом, при этом индексы совпавших записываются в строку (присоединяются к пустой строке)
        if mlist[i] == k:
            mstring += (str(mlist.index(k)) + ' ')
            mlist[i] = ' '
            i += 1
        else:
            i += 1
print(mstring)