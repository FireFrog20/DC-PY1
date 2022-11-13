from pprint import pprint  # импортируем pprint из модуля pprint


end = 15  # До какого числа создаём наши словари
pprint([{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(end+1)])  # При помощи list
# comprehenshion создаём список словарей нужного вида, используя созданный вручную шаблонный словарь в качестве
# элемнта списка и печатаем ответ при помощи импортированной функции pprint из модуля pprint

