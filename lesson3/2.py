def print_info(name, surname, year, city, email, phone):
    print(f'Имя:{name},Фамилия:{surname}, Год рождения:{year}, Город проживания:{city},Электронная почта:{email},Телефон:{phone}')
name = input("Введите имя:")
surname = input("Введите фамилию:")
year = input("Введите год рождения:")
city = input("Введите город проживания:")
email = input("Введите электронную почту:")
phone = input("Введите телефон:")

print_info(name, surname, year, city, email, phone)

