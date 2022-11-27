OUTPUT_FILE = "output.csv"  # имя файла для записи данных


# TODO реализовать функцию to_csv_file
def to_csv_file(filename: str, headers: list[str], rows: list[list[str]], delimiter=",", newline="\n") -> None:  #
    # инициализируем функцию, задаём переменныее с их типами и значениями по умолчанию, задаём тип return
    with open(filename, "w", encoding="utf-8") as f:  # Открываем .csv файл с заданным именем в режиме записи и
        # кодировке utf-8
        f.write(delimiter.join(headers) + newline)  # Записываем в файл заголовки, передавая заданный пользователем
        # список строк методу join с заданным разделителем
        f.writelines(delimiter.join(item) + newline for item in rows)  # аналогично записываем сами данные, доставая
        # списки строк из заданного списка списков при помощи list comprehension


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population',
                'households', 'median_income', 'median_house_value']  # заголовки
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500',
     '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000',
     '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400',
     '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900',
     '330000.000000'],
]  # данные

# TODO вызвать функцию to_csv_file и записать данные в файл

to_csv_file(OUTPUT_FILE, headers_list, data)  # вызываем нашу функию, передавая ей имя файла для записи, заголовки и
# сами данные, остальные параметры оставляем по умолчанию

with open(OUTPUT_FILE) as output_f:  # Снова открываем наш файл
    for line in output_f:  # "пробегаем" по его содержимому
        print(line, end="")  # и выводим информацию при помощи функции print
