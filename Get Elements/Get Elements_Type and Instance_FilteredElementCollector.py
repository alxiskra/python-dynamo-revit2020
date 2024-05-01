# Method - OfCategory (BuiltInCategory.category) - возвращает список всех элементов категории
# Method - ToElements() - получить элементы прошедшие фильтры
# Method - WhereElementIsElementType() - фильтр: где элемент является типом элемента
# Method - WhereElementIsNotElementType() - фильтр: где элемент является экземпляром элемента

import clr
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

doorTypes = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsElementType().ToElements()
doorInstances = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()

OUT= doorTypes