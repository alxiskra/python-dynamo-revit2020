#### Функция для копирования строк в буфер обмена ####
# если переменная data является списком и все его элементы являются строками, то выполнить следующий блок кода
## The isinstance(x,y) function checks if the object (first argument) is an instance or subclass of classinfo class (second argument). 
## isinstance() проверяет принадлежность объекта к классу или типу данных. принимает два аргумента: объект, который нужно проверить, и класс или тип данных, к которому нужно проверить принадлежность
## all(iterable) - функция проверяет, все ли элементы в итерируемом объекте являются истинными (равны True)
### Преобразование списка строк в одну строку с использованием перевода строки в качестве разделителя
### Копирование строки в буфер обмена
### join() - метод для слияния списка. Пример: если "_".join(list) то получим объединенный список "El[0]_El[1]_El[2]..."
### Символ новой строки: \n
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Clipboard

def copy_to_clipboard ( data ) :
	if isinstance( data, list ) and all( isinstance( element, str ) for element in data ):
		text_to_copy = '\n'.join(data)
		Clipboard.SetText(text_to_copy)
		return "Успех: Список строк скопирован в буфер обмена"
	if isinstance( data, str ):
		text_to_copy = data
		Clipboard.SetText(text_to_copy)
		return "Успех: Строка скопирована в буфер обмена"
	else:
		return "Ошибка: На вход нужно подать одноуровневый список"

data = IN[0]
result = copy_to_clipboard(data)
OUT = result