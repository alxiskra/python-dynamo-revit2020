import clr
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, ParameterValueProvider, ElementId, FilterStringContains, ElementParameterFilter, FilterStringRule, Transaction
doc = DocumentManager.Instance.CurrentDBDocument
fec = FilteredElementCollector
param = BuiltInParameter.ALL_MODEL_MARK
provider = ParameterValueProvider(ElementId(param))
evalCon = FilterStringContains()
evaluator = evalCon

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

from Autodesk.Revit.DB import UnitUtils

# Преобразование значений из мм в единицы Revit
depth1_internal = [UnitUtils.ConvertToInternalUnits(value, Autodesk.Revit.DB.DisplayUnitType.DUT_MILLIMETERS) for value in depth1]
depth2_internal = [UnitUtils.ConvertToInternalUnits(value, Autodesk.Revit.DB.DisplayUnitType.DUT_MILLIMETERS) for value in depth2]

# Открытие транзакции
transaction = Transaction(doc, "Set Parameters")
transaction.Start()

# Установка значений параметров для каждого элемента
for i, el in enumerate(elements):
    el.LookupParameter("Глубина лотка 1").Set(depth1_internal[i])
    el.LookupParameter("Глубина лотка 2").Set(depth2_internal[i])

# Завершение транзакции
transaction.Commit()


# Пример возвращения значений обратно в мм
#depth1_mm = [UnitUtils.ConvertFromInternalUnits(value, Autodesk.Revit.DB.DisplayUnitType.DUT_MILLIMETERS) for value in depth1_internal]
#depth2_mm = [UnitUtils.ConvertFromInternalUnits(value, Autodesk.Revit.DB.DisplayUnitType.DUT_MILLIMETERS) for value in depth2_internal]

OUT = elements