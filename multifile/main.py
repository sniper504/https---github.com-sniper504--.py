import circle  as circ
import is_even  as even
import sum_diligits  as dil
import temperature  as temp

def main():
    user_input = input("Выберите что вы хотите сделать :\n функция 1 переводит температуру из гадусов цельсий в форенгейты \n  функция 2 считает сумму цифр числа \n  функция 3 проверяет четность числа \n  функция 4 находит площадь круга и длину окружнности используя радиус \n  введите номер операции")
    if user_input == '1':
        temp.main()
    elif user_input == '2':
        dil.main()
    elif user_input == '3':
        even.main()
    elif user_input == '4':
        circ.main()
           
if __name__ == '__main__':
    main()


