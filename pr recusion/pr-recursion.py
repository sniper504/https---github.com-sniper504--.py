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
    if N ==0:
        return 0
    if len(N)==0:
        return N
    if 
        return sum_diligits() + 
print("введите число")
user_input=input()
result_fac=factorial(user_input)
print("Факториал вашего числа равен",result_fac)
result_fib=fibonachi(user_input)
print("номер элемента вашего числа в ряде Фибоначи:",result_fib)