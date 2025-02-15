import numpy as np
#1
var1 = np.array([1, 4, 6])
var2 = np.array([1, 4, 6])

arrays_equal = np.array_equiv(var1, var2)
print(arrays_equal)

#2
def check():
    list1 = []
    list2 = []

    for v1 in range(11):
        v1 = int(input('Введите число от 1 до 10: '))
        if v1 < 10 and v1 != 0:
          print('Вы ввели корректное значение')
          if len(list1) != 3:
              list1.append(v1)
              if len(list1) == 3:
                  print(list1, '-List1 сформирован!')
          elif len(list2) != 3:
              list2.append(v1)
              if len(list2) == 3:
                  print(list2, '-List2 сформирован!')
                  break
          #elif len(list2) == 3:
             #break
        else:
          print('Вы ввели некорректное значение, попробуйте снова!')
          continue
    if list1 == list2:
        print('True - cписки идентичны')
    else:
        print('False - списки неидентичны')
check()



