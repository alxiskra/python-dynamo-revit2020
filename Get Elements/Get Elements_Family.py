# функция set() преобразует список [] в множество {}, это позволяет получить уникальные элементы

import clr
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

# Получаем экземпляры дверей
doorInstances = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()
# Собираем идентификаторы семейств дверей
familyIds = set([doorInstance.Symbol.Family.Id for doorInstance in doorInstances])
# Получаем семейства дверей
doorFamilies = [doc.GetElement(familyId) for familyId in familyIds]

OUT = doorFamilies