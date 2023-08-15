working_hours: str = int(input('Введите количество отработанных часов в месяц:'))  

hourly_rate: str = input('')  

salary: int = hourly_rate * working_hours

print('Ваша почасовая ставка:', working_hours, 'рублей')  
print('Заработная плата в месяц:', salary, 'рублей')