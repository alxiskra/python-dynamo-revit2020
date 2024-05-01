# Функция для копирования строк в буфер обмена
# если переменная data является списком и все его элементы являются строками, то выполнить следующий блок кода

# isinstance() проверяет принадлежность объекта к классу или типу данных. принимает два аргумента: объект, который нужно проверить, и класс или тип данных, к которому нужно проверить принадлежность
# all(iterable) - функция проверяет, все ли элементы в итерируемом объекте являются истинными (равны True)

# join() - метод для слияния списка. Пример: если "_".join(list) то получим объединенный список "El[0]_El[1]_El[2]..."
# Символ новой строки: \n

# если нужно преобразовать входные данные в string то используем str() например в строке:
# text_to_copy = '\n'.join(', '.join(str(element) for element in sublist) for sublist in zip(*data))

import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Clipboard

list_separator = "; "

def copy_to_clipboard(data):
    if isinstance(data, list) and all(isinstance(sublist, list) for sublist in data):
        # Обработка списка списков
        text_to_copy = '\n'.join(list_separator.join(element for element in sublist) for sublist in zip(*data))
        Clipboard.SetText(text_to_copy)
        return "Успех: Список списков скопирован в буфер обмена"
    elif isinstance(data, list) and all(isinstance(element, str) for element in data):
        # Обработка одиночного списка строк
        text_to_copy = '\n'.join(data)
        Clipboard.SetText(text_to_copy)
        return "Успех: Список строк скопирован в буфер обмена"
    elif isinstance(data, str):
        # Обработка одиночной строки
        Clipboard.SetText(data)
        return "Успех: Строка скопирована в буфер обмена"
    else:
        return "Ошибка: На вход нужно подать строку или список списков строк"

data = IN[0]
result = copy_to_clipboard(data)
OUT = result