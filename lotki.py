# Импортируем необходимые модули
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
>>>>>>> 39aaaed5ee95f0a3871e041abbe542518853b5cf

<<<<<<< HEAD
value = IN[0]

caseSensitive = False
rule = FilterStringRule(provider, evaluator, value, caseSensitive)
filter = ElementParameterFilter(rule)
analyticalCollector = fec(doc).WherePasses(filter).ToElements()

key = list(el.LookupParameter("Комментарии").AsString() for el in analyticalCollector)
tuple = zip(key, analyticalCollector)
elements = [el for _, el in sorted(tuple)]

# x2 = x1-(y*L)/100
# уклон = (x1-x2)/l*100
# Функция для вычисления глубины для каждого элемента
def compute_depths(element_count, depth_initial, element_length, slope):
    depth1 = []
    depth2 = []
    # Начальная глубина для первого элемента
    depth1.append(depth_initial)
    depth2.append(depth_initial - (slope * element_length) / 100)
    # Вычисляем глубину для остальных сегментов
    for i in range(1, element_count):
        x0 = depth2[-1]
        x2 = x0 - (slope * element_length) / 100
        depth1.append(x0)
        depth2.append(x2)
    return depth1, depth2

# Вводные данные
depth_initial = IN[1]   # Начальная глубина для первого элемента
element_length = IN[2]  # Длина элемента
slope = IN[3]           # Уклон
element_count = len(elements)       # Количество элементов

# Вычисляем глубины для каждого элемента
depth1, depth2 = compute_depths(element_count, depth_initial, element_length, slope)

# Формируем список значений параметров для каждого элемента
output = [depth1, depth2]

for el in elements:
    el.LookupParameter("Глубина лотка 1").Set(depth1[i])
    el.LookupParameter("Глубина лотка 2").Set(depth2[i])

OUT = elements
=======
# x2 = x1-(y*L)/100
# уклон = (x1-x2)/l*100

# Функция для вычисления глубины для каждого элемента
def compute_depths(element_count, depth_initial, element_length, slope):
    depth1 = []
    depth2 = []
    
    # Начальная глубина для первого элемента
    depth1.append(depth_initial)
    depth2.append(depth_initial - (slope * element_length) / 100)
    
    # Вычисляем глубину для остальных сегментов
    for i in range(1, element_count):
        x0 = depth2[-1]
        x2 = x0 - (slope * element_length) / 100
        depth1.append(x0)
        depth2.append(x2)

    return depth1, depth2

# Пример вводных данных
depth_initial = IN[0]  # Начальная глубина для первого элемента
element_length = IN[1]  # Длина элемента
slope = IN[2]  # Уклон
element_count = 5  # Количество элементов

# Вычисляем глубины для каждого элемента
depth1, depth2 = compute_depths(element_count, depth_initial, element_length, slope)

# Формируем список значений параметров для каждого элемента
output = [depth1, depth2]

# Возвращаем список значений параметров
OUT = output

>>>>>>> 39aaaed5ee95f0a3871e041abbe542518853b5cf