# выводит часть последовательности 
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... 
# (число повторяется столько раз, чему равно)
n = int(input()) 
r = 1
mlist = []
mmlist = []
for i in range(n):
    mlist.append([]) #создаем массив mlist и заполняем его пустыми массивами в качестве элементов
    for j in range(r):
        mlist[i].append(r)#заполняем каждый пустой массив внутри mlist одинаковыми числами (значение счетчика r)
    r += 1 #увелиыиваем значение счетчика на 1 для каждого влоденного массива в mlist
for i in range(len(mlist)): #создаем из двухмерного массива mlist одномерный mmlist
    for j in range(len(mlist[i])):
        mmlist.append(mlist[i][j])
print(*mmlist[0:n])# выводим в строку все элементы среза массива mmlist разделенные пробелом