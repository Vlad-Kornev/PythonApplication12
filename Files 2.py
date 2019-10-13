with open ('file.txt', 'r') as inf:
    s1 = inf.readline()
    s2 = inf.readline()
# Функция strip убирает из считываемой строки специальные символы (табуляции и т.д.)
print (s1.strip(),s2.strip(), sep = '\n')
