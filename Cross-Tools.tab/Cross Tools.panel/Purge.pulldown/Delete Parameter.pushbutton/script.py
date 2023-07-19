from revitutils import doc

# noinspection PyUnresolvedReferences
from Autodesk.Revit.DB import Transaction, FilteredElementCollector, ParameterElement

#Retrieve all parameters in the document
params = FilteredElementCollector(doc).OfClass(ParameterElement)
filteredparams = []

#Store parameters which has a name starting with "magi" or "MC"
for param in params:
    if param.Name.startswith(("magi", "MC")): #startswith method accept tuple
        filteredparams.append(param)
        print param.Name

#Delete all parameters in the list
t = Transaction(doc, "Delete parameters")
t.Start()
for param in filteredparams:
    doc.Delete(param.Id)
t.Commit()