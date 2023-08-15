line: str = input('Введите строку: ')
num: int = int(input('Введите число: '))

result: str = (line + '\n') * num

print(result, end='')
