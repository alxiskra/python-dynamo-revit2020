#если нужна сортировка в алфавитном порядке то использовать sorted()
#OUT = sorted(catnames)
#чтобы получить категории на английском языке нужно запустить ревит в версии ENU

import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument

list = doc.Settings.Categories
catnames = []
for el in list:
	catnames.append(el.Name)

OUT = catnames