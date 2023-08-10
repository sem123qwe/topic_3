working_hours: int = 176  

hourly_rate: int = int(input
                       ('Введите количество отработанных часов в месяц:')
                       )  

salary: int = hourly_rate * working_hours

print('Ваша почасовая ставка:',working_hours,'рублей')  
print('Заработная плата в месяц:',salary,'рублей')

# TODO: Исправить ошибки по PEP8
#  - решить через input()
#  - реализовать правильную логику


