a = int(input())
b = int(input())
c = int(input())
d = int(input())

# вывод первой строки таблицы (числа от c до d), 
for j in range (c,d+1):
# добавлен отступ вначале - "\t" и вывод в одну строку - "end = ''"
    print ('\t',j,end = '')
# перевод в конце цикла на новую строку
print()

# построчный вывод оставшейся части таблицы
for i in range (a,b+1):
    # вывод цифр в первом столбике (от a до B) без перевода на новю строку
    print (i,' ', end ='')
    #вывод произведений i*j такэе в одну строку для каждой итерации
    for j in range (c,d+1):
        print ((i*j),' ',end = '')
    #переход на новую строку после каждой итерации
    print()
    




 #   a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#for i in range (c,d+1):
#    print ('\t',i,end = '')
#for j in range (a,b+1):
 #   print ()
  #  print (j,'\t',end = '')
   # for k in range (c,d+1):
    #    print (j*k,'\t',end = '')