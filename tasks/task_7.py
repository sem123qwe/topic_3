hourly_rate: float = float(input())

working_hours: int = 176  # 22 * 8

salary: float = hourly_rate * working_hours

print('Вы проработали', working_hours, 'часов')
print('Ваша зарплата', salary, 'рублей')
