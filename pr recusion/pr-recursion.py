def factorial(N):
    if N==0:
        return 1
    if N==1:
        return 1
    else:
        return factorial(int(N)-1)*int(N)
def fibonachi(N):
    if N == 0:
        return 0
    if N in (1, 2):
        return 1
    return fibonachi(int(N) - 1) + fibonachi(int(N) - 2)
def sum_diligits(N):
    if len(N) ==1:
        return int(N)
    if len(N)>1:
        return int(N[0]) + sum_diligits(N[1:])
def degree2(N): 
    if N == 0:
        return False
    if int(N) % 2 == 0:
        return int(N[0]) + degree2(N[1:])
    return degree2(N // 2)
def output():
    if degree2(user_input):
        print("число является степенью двойки")
    else:
        print("число не является степенью двойки")
def is_power_of_two(N):
    if int(N) == 1:
        print("число является степенью двойки")
    elif int(N) == 0 or int(N) % 2 != 0:
        print("число не является степенью двойки")
    else:
        is_power_of_two(int(N) // 2)
print("введите число")
user_input=input()
result_fac=factorial(user_input)
print("Факториал вашего числа равен",result_fac)
result_fib=fibonachi(user_input)
print("номер элемента вашего числа в ряде Фибоначи:",result_fib)
result_sum=sum_diligits(user_input)
print("сумма цифр числа равна",result_sum)
result_degree=is_power_of_two(user_input)



