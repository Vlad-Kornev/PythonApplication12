#a = 0
#while a <= 7:
 #   print ('*' * a)
  #  a += 1

# альтернатиыный вариант решения задачи с выводом треугольника
# из звездочек

n = int(input())
stars = '*'
while len(stars) <= n:
    print (stars)
    stars += '*'
