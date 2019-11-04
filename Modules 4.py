import tkinter,requests
from tkinter.filedialog import*
st = 'https://stepic.org/media/attachments/course67/3.6.3/'

# функция для проверки наличи слова "we" в начале файла
def f_check(n):
    st = 'https://stepic.org/media/attachments/course67/3.6.3/'
    r = requests.get(st+n)
    ar = r.text.split()
    return (ar[0])

# открытие первого файла для получения первой ссылки
w = Tk()
w.title('Выбор файла для анализа')
f = askopenfile('r')
w.destroy()
first_url = f.readline().strip()
r = requests.get(first_url)
na = r.text

# цикл для последовательной проверки всех файловЫ
while f_check(na) != 'we':
    r = requests.get(st + na)
    na = r.text
    print (na)
with open('text1.txt','w') as inf:
    print(na, file = inf)