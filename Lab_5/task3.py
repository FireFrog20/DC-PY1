from random import choice  # Импортируем функцию choice из модуля random


def get_unique_list_numbers(beginning_: int, end_: int, amount_: int) -> list[int]:  # инициализируем нашу функцию и
    # производим аннатацию типов аргументов

    if end_ - beginning_ + 1 < amount_:  # Проверяем возможно ли создание уникального списка запрашиваемого размера
        # из заданного диапозона чисел
        raise ValueError("Невозможно создать список, так как уникальных значений в заданном диапозоне меньше чем "
                         "требуется для создания списка")  # В случае отсутствия возможности поднимаем ошибку
    ans = []  # пустой лист для записи ответа
    bag = list(range(beginning_, end_+1))  # лист из всех чисел (наш своеобразный "мешок" из которого будем случайно
    # вытискивать значения)
    for _ in range(amount_):  # в цикле достаём из "мешка" числа
        chosennumber = choice(bag)  # достаём из "мешка" число
        ans.append(chosennumber)  # добавляем его в ответ
        bag.remove(chosennumber)  # удаляем его из "мешка", чтобы не повторяться
    return ans  # возвращаем итоговый список уникальных чисел






list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
