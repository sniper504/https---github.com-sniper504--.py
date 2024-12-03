def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
print("Введите число") 
n = input()
print("сумма цифр в числе")
print(getSum(n))