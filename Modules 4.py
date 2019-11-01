import tkinter
from tkinter.filedialog import*
w = Tk()
w.title('Выбор файла для анализа')
f = askopenfile('r')
w.destroy()
for line in f:
    print(line)