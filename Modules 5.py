import tkinter
from tkinter.filedialog import *
win = Tk()
win.title('Выбор файла')
f = askopenfile('r')
win.destroy()
main_dict = {}#основной словарь, в нем командам соответствует списко из кол-ва побед, ничьих, поражений и т.д.
goal_dict = {}
# созданик функции, которая на основании каждой строки будет заполнять словарь и списки, соответствующие элементам словаря
def func_lines(line):
    a = line.strip().split(sep=';')
    if a[0] not in main_dict.keys():
        main_dict.setitem(a[0])


for line in f:
    if len(line.strip()) == 1:
        games = int(line)
        # определяем количество игр
    else:
        print(line.strip().split(sep=';'))
        func_lines(line)
        print(main_dict)