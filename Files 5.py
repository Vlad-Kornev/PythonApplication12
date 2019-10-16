a = []
b = []
cm = 1
with open('file.txt') as inf:
# создание списка слов из текстовых строк в файле    
    for line in inf:
        a += line.strip().lower().split()
# поиск наибольшего числа вхождений слов в текст
for n in a:
    if a.count(n) > cm:
        cm = a.count(n)
# поиск лексиграфически первого слова
for n in a:
    if a.count(n) == cm:
        b.append(n)
mx = min(b)
print (mx, cm)