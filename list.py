#21. Объединить Два Сортированных Списка



def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

# Проверяем, что оно работает
list1 = [1, 2, 5, 8, 9]
list2 = [3, 4, 7, 10, 11]

list1.extend(list2)
bubble_sort(list1)
print(list1)


