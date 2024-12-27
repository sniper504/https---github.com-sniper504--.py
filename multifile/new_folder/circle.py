#написать код для вычисления площади круга через радиус  длину окружности через радиус через функцию def
#написать код для вычисления длины окружности через радиус через вункцию def
#========================================================================================================

def square(radius):
    s=3.14*float(radius)**2
    return(s)

def length(radius):
    l=2*3.14*int(radius)
    return(l)
def main():
    print("введите радиус")
    radius=input()

    result=square(radius)
    print("площадь круга")
    print(result)

    result=length(radius)
    print("длина окружности")
    print(result)

if __name__ == '__main__':
    main()