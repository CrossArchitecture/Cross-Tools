import rpw
doc = rpw.revit.doc
uidoc = rpw.revit.uidoc

# noinspection PyUnresolvedReferences
from Autodesk.Revit.DB import Transaction, FamilySymbol

__doc__ = "Delete selected families from project"
__title__ = "Delete Family"
__author__ = "Erich Domme"


with rpw.db.Transaction("Delete families from project"):
    # Find families of selected object and delete it
    for id in uidoc.Selection.GetElementIds():
        el = doc.GetElement(id)
        family_id = el.Symbol.Family.Id
        doc.Delete(family_id)



