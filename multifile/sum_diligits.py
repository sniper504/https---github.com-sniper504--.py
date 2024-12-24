# написать код для нахождения суммы цифр в числе путем функции def
#=================================================================

def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
def main():
  print("Введите число") 
  n = input()
  print("сумма цифр в числе")
  print(getSum(n))

if __name__ == '__main__':
  main()