import string
from random import sample  # Импортируем функцию choice из модуля random


def get_random_password(n: int) -> str:  # инициализируем нашу функцию и производим аннатацию типов аргументов
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits  # Алфавит для наших паролей
    if n > len(alphabet):  # Проверяем, что пароль не слишком длинный
        raise ValueError("Требуемый пароль больше базы символов")  # Если это так вызываем ошибку
    return "".join(sample(alphabet, n))  # Возвращаем пароль


print(get_random_password(8))
