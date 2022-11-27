import json  # импортируем моудль для работы с форматом json

INPUT_FILE = "input.csv"  # имя файла, из которого будем читать данные


def csv_to_list_dict(filename: str, delimiter=",", newline="\n") -> list[dict]:  # инициализируем функцию, задаём
    # переменныее с их типами и значениями по умолчанию, задаём тип return
    with open(filename, "r", encoding="utf-8") as f:  # Открываем .csv файл с заданным именем в режиме чтения и
        # кодировке utf-8
        data_ = [item.strip(newline).split(delimiter) for item in f]  # Читаем содержимое нашего файла, функцией
        # strip удаляем заданный символ конца строки, функцией split разбиваем строку по заданному разделителю на
        # список строк и при помощи list comprehension записываем эти списки в список
        return [{data_[0][i]:item[i] for i in range(len(data_[0]))} for item in data_[1:]]  # Возвращаем список
        # словарей на основании прочитанного из файла списка списков, для этого используем dict comprehension и list
        # comprehension (заголовки, они же ключи для наших словарей хранятся в data_[0], поэтому в list comprehension
        # "пробегаем" список не с 0, а с 1 позиции)

        # return [dict(zip(data_[0], item)) for item in data_[1:]]  # Или проводим аналогичную операцию
        # используя list comprehension и функции dict и zip


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))  # Вызываем нашу функцию, передавая ей имя файла, остальные
# параметры оставляем по умолчанию; переводим наш список словарей в JSON-строку с нужными отступами при помощи метода
# dumps из модуля json и выводим информацию при помощи print

