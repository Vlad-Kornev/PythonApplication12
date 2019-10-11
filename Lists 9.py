# Задача - вывести таблицу размерности n x n заполненную числами от 1 до n2 по спирали, закрученной по часовой стрелке
n = int(input('введите число для построения таблицы'))
# вводим переменную k, являющуюся дополнительным счетчиком, используемым при повороте спирали на внутренних витках (т.е. после заполнения внешнего периметра матрицы)
k = n
mlist = [[0 for x in range(n)] for y in range(n)]
# переменная st является счетчиком, используемым для хранения значений внутри ячеек таблицы
st = 1
x,y = 0,0
while st <= n**2:
    #верхний горизонтальный проход спирали, слева направо
    for x in range(n-k,k):
        mlist[y][x] = st
        st += 1
    #правый вертикальный проход спирали, сверху вниз
    for y in range((n-k)+1,k):
        mlist[y][x] = st
        st += 1
    #нижний горизонтальный проход спирали, справа налево
    for x in range(k-2,n-k-1,-1):
        mlist[y][x] = st
        st += 1
    #правый горизонтальный проход спирали, снизу вверх
    for y in range(k-2,n-k,-1):
        mlist[y][x] = st
        st += 1
    #уменьшаем значение счетчика K чтобы релизовать цикл заполнения внутренних витков спирали
    k -= 1
for m in mlist:
    print (*m)