name: str = input('Введите ваше имя: ')
surname: str = input('Введите вашу фамилию: ')
age: int = int(input('Введите ваш возраст: '))

custom_sep: str = ''

print('Тип имени: ', type(name),
      ', ID в памяти: ', id(name), sep=custom_sep)
print('Тип фамилии: ', type(surname),
      ', ID в памяти: ', id(surname), sep=custom_sep)
print('Тип возраста: ', type(age),
      ', ID в памяти: ', id(age), sep=custom_sep)
