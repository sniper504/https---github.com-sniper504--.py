##написать код для нахождения температуры через функцию Def
# написать код ля нахождения температупы в форенгейтах через функцию def
#======================================================================

def temperature(a):
    t=(float(a)*9/5)+32
    return(t)
def main():
    print('Введите значение')
    a=input()
    t=temperature(a)
    print("температура в форенгейтах")
    print(t)

if __name__ == '__main__':
    main()

