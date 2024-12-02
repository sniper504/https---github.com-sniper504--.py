import random

# Генерация списка из 100 случайных целых чисел от 0 до 1000000
numbers = [random.randint(0, 1000000) for _ in range(100)]
print("Исходный список:", numbers)

# Сортировка пузырьком
print("\nСортировка пузырьком:")
bubble_numbers = numbers.copy()
bubble_comparisons = 0  # Счетчик сравнений
n = len(bubble_numbers)

for i in range(n):
    for j in range(0, n-i-1):
        bubble_comparisons += 1
        if bubble_numbers[j] < bubble_numbers[j+1]:  # Сортировка в порядке убывания
            bubble_numbers[j], bubble_numbers[j+1] = bubble_numbers[j+1], bubble_numbers[j]
    print(f"Шаг {i + 1}: {bubble_numbers}")

print("Отсортированный список (пузырьком):", bubble_numbers)
print("Количество сравнений (пузырьком):", bubble_comparisons)

# Сортировка выбором
print("\nСортировка выбором:")
selection_numbers = numbers.copy()
selection_comparisons = 0  # Счетчик сравнений
n = len(selection_numbers)

for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        selection_comparisons += 1
        if selection_numbers[j] > selection_numbers[max_index]:  # Сортировка в порядке убывания
            max_index = j
    selection_numbers[i], selection_numbers[max_index] = selection_numbers[max_index], selection_numbers[i]
    print(f"Шаг {i + 1}: {selection_numbers}")

print("Отсортированный список (выбором):", selection_numbers)
print("Количество сравнений (выбором):", selection_comparisons)