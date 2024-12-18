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
print("введите число")
user_input=input()
result_fac=factorial(user_input)
print("Факториал вашего числа равен",result_fac)
result_fib=fibonachi(user_input)
print("номер элемента вашего числа в ряде Фибоначи:",result_fib)
result_sum=sum_diligits(user_input)
print("сумма цифр числа рвна",result_sum)