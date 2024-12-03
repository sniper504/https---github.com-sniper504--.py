import random
# Создание списка из 100 случайных целых чисел от 0 до 1_000_000
numbers = [random.randint(0, 1000000) for _ in range(100)]
print("Исходный список:", numbers)



# Сортировка пузырьком
print("Сортировка пузырьком:")
bubble_numbers = numbers.copy()
# Счетчик сравнений 
bubble_counter = 0 
#длинна списка для сортирвки пузырьком
bubble_length = len(bubble_numbers)
#начало сотрировки
for i in range(bubble_length):
    for j in range(0, bubble_length-i-1):
        bubble_counter += 1
        # Сортировка в порядке убывания
        if bubble_numbers[j] < bubble_numbers[j+1]:
            #меняем местами большее и меньшее
            bubble_numbers[j], bubble_numbers[j+1] = bubble_numbers[j+1], bubble_numbers[j]
    print(f"Шаг {i + 1}: {bubble_numbers}")
print("Отсортированный список (пузырьком):", bubble_numbers)
print("Количество сравнений (пузырьком):", bubble_counter)
# Сортировка выбором




print("Сортировка выбором:")
selection_numbers = numbers.copy()
# Счетчик сравнений
selection_counter = 0  
#длинна списка для сортировки выбором
selection_length = len(selection_numbers)
#начало сортировки
for i in range(selection_length):
    max_index = i
    for j in range(i + 1, selection_length):
        selection_counter += 1
        # Сортировка в порядке убывания
        if selection_numbers[j] > selection_numbers[max_index]: 
            max_index = j
            #меняем местами элементы
    selection_numbers[i], selection_numbers[max_index] = selection_numbers[max_index], selection_numbers[i]
    print(f"Шаг {i + 1}: {selection_numbers}")
print("Отсортированный список (выбором):", selection_numbers)
print("Количество сравнений (выбором):", selection_counter)