import tkinter
from tkinter.filedialog import *
root = Tk()
root.update()
inf = tkinter.filedialog.askopenfile('r')
root.destroy()
for line in inf:
    print(line)
inf.close()
