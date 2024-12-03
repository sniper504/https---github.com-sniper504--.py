import random
# Генерация уникальных случайных чисел и сортировка
numbers = random.sample(range(0, 1000000), 100)
numbers.sort()
print("Отсортированный список:", numbers)

# Заданный элемент для поиска
target = int(input("Введите число для поиска: "))



# Линейный поиск
index_linear = -1
comparisons_linear = 0  # Счетчик сравнений

for index in range(len(numbers)):
    comparisons_linear += 1
    if numbers[index] == target:
        index_linear = index
        break  # Выход из цикла, если элемент найден

# Результаты линейного поиска
if index_linear != -1:
    print(f"Элемент {target} найден на индексе {index_linear}.")
    print(f"Количество сравнений (линейный поиск): {comparisons_linear}")
else:
    print(f"Элемент {target} не найден.")
    print(f"Количество сравнений (линейный поиск): {comparisons_linear}")



# ---------------------------------------------
# Бинарный поиск
index_binary = -1
comparisons_binary = 0  # Счетчик сравнений
left, right = 0, len(numbers) - 1

while left <= right:
    comparisons_binary += 1
    mid = left + (right - left) // 2
    
    if numbers[mid] == target:
        index_binary = mid
        break  # Выход из цикла, если элемент найден
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Результаты бинарного поиска
if index_binary != -1:
    print(f"Элемент {target} найден на индексе {index_binary}.")
    print(f"Количество сравнений (бинарный поиск): {comparisons_binary}")
else:
    print(f"Элемент {target} не найден.")
    print(f"Количество сравнений (бинарный поиск): {comparisons_binary}")