money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить

while money_capital - (spend - salary) >= 0:  # Живём до тех пор пока не кончится подушка
    month += 1
    money_capital = money_capital - (spend - salary)   # в конце месяца вычитаем разницу между тратами и зарплатой из
    # подушки
    spend = spend * (1 + increase)

# Альтернативный вариант с ответом 3

#while money_capital >= spend:  # Живём до тех пор пока подушка покрывает расходы
#    month += 1
#    money_capital = money_capital + salary - spend
#    spend *= (1 + increase)



print(month)
