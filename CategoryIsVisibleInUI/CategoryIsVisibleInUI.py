#https://forums.autodesk.com/t5/revit-api-forum/get-revit-model-categories-as-in-the-object-styles-dialog/td-p/9979578

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
cats = doc.Settings.Categories

def CategoryIsVisibleInUI(cat):
	if hasattr(cat, "IsVisibleInUI"):
		return cat.IsVisibleInUI
	else: return "None"

OUT = [CategoryIsVisibleInUI(el) for el in cats]
