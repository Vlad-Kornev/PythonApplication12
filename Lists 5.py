# Программа принимает на вход целые числа по одному до того момента,
# пока сумма ранее введенных чисел не будет равна 0, после чего 
# программа выводит сумму квадратов ранее введенных чисел

mylist = []
s = int(input())
mylist.append(s)
m = 0
while s != 0:
     a = int(input())
     mylist.append(a)
     s += a
for n in mylist:
    m += (n * n)
print(m)