# ввод значений a и b
a = int(input())
b = int(input())

# переменная, в которой хранятся значения
p = 1
pm = a * b

while (p <= pm):
    if ((p % a) == 0) and ((p % b) == 0):
        print (p)
        break
    else:
        p += 1


# альтернатиыный вариатнт решения задачи - использовать оператор or

#a = int(input())
#b = int(input())
#s = 1
#while (s % a != 0) or (s % b != 0) == True:
#    s += 1
#print (s)