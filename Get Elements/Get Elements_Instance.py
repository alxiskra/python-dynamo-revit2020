# extend() - берет каждый элемент внутри принимаемого списка и кладет его в список
# append() - берет принимаемый список и кладет его в список
# https://forums.autodesk.com/t5/dynamo-russkiy-tolko-dlya-chteniya/vybor-elementov-iz-raznyh-kategoriy-v-python-e/td-p/8750426

import clr
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

elements = []

catNames = 'OST_Walls,OST_Floors,OST_Rooms,OST_Doors'.split(',')

for el in catNames:
	exec('cat = BuiltInCategory.'+el)
	elements.extend(FilteredElementCollector(doc).OfCategory(cat).WhereElementIsNotElementType().ToElements())

OUT = elements