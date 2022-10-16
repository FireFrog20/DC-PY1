src = not False and True or False and not True

# TODO расписать упрощение выражения
# result = True and True or False and False # Избавляемся от отрицаний
# result = true or false # Избавляемся от логических "И"
# result = true # Избавляемся от логического "ИЛИ"
result = True  # TODO подставить результат выражения

print(src == result)
