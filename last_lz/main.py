# импортируем модули
import life_zone as zone
import new_folder_pyramid as pyramid

def main():# делаем выбор
    user_input = input("Выберите что вы хотите сделать :\n функция 1 определяет средний радиус обитаемой зоны вокруг звезды по формуле \n функция 2 определяет обьем усеченной пирамиды \n выберите нужную операцию" )
    if user_input == '1':
            zone.main()
    if user_input == '2':
            pyramid.main()

if __name__ == '__main__':
    main()