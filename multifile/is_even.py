#написать код для прочерки четности числа через функцию def
#==========================================================

def definition(a):
    if int(a) % 2==0:
        return True
    else:
       return False
def main():
    print("Введите число")
    a=input()
    definition(a)
    result =definition(a)
    if result is True:
         print("четное")
    else:
         print("не четное")     
    
if __name__ == '__main__':
    main()
