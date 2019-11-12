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
    for n in line:
        if n.isalpha == True:
            if n not in main_dict == True:
                        main_dict[n] = []
            else:
                continue
        else:
















for line in f:
    if len(line.strip()) == 1:
        games = int(line)
        # определяем количество игр
    else:
        print(line.strip().split(sep=';'))
