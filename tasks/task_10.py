name = input('Введите ваше имя:')
surname = input('Введите вашу фамилию:')
age = int(input('Введите ваш возраст:'))  

custom_sep = ''

print('Тип имени:', type(name), ', ID в памяти:', id(name),sep = custom_sep)    # допишите код
print('Тип фамилии:', type(surname), ', ID в памяти', id(surname), sep = custom_sep)  # допишите код
print('Тип возраста:', type(age),', ID в памяти:', id(age), sep = custom_sep)  # допишите код
