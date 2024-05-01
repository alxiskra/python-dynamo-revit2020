# https://forums.autodesk.com/t5/revit-i-navisworks-russkiy/vnutrennie-imena-kategoriy-revit/td-p/9026714

# try - в данный блок помещается код который при выполнии может получить ошибку
# except - в данный блок помещается код для обработки ошибки
# например: except TypeError: *блок кода для выполнения в случае ошибки типа*
# pass - в данном контексте позволяет пропустить элементы обработка которых невозможна
# также в try возможны else и finally

import clr, System
clr.AddReference("RevitNodes")
import Revit
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
 
bic = System.Enum.GetValues(BuiltInCategory)
cats, bics = [], []
for el in bic:
    try:
        cat = Revit.Elements.Category.ById(ElementId(el).IntegerValue)
        cats.append(cat)
        bics.append(el)
    except:
        pass
        
OUT = bics,cats