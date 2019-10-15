with open('file.txt','r') as inf:
    s = inf.readline().strip()
sym = '' # переменная в которой будет хранится последний считанный символ
num = '' # переменная в которой будет хранится число повторений символа
res = '' # результат одной итерации цикла
ires = ''# итоговая распакованная строка
i = 0
while i <= len(s) - 1:
    # проверка, является ли символ буквой
    if s[i].isalpha():
        sym = s[i]
        res = s[i]
        st = 1
    else:
        # проверка, является ли количесво повторений буквы двухзначным числом
        if (i+1) <= (len(s)-1): # дополнительная проверка на случай ошибки IndexError, когда проверяется [i + 1] символ строки
            if s[i+1].isdigit():
                num = s[i] + s[i+1]
                res = sym * (int(num) - 1)
                st = 2
            else:
                num = s[i]
                res = sym * (int(num) - 1)
                st = 1
        else:
            num = s[i]
            res = sym * (int(num) - 1)
            st = 1
    ires += res
    i += st
with open('file1.txt','w') as inf1:
    inf1.write(ires)