import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import Document, CentralModelPath, WorksharingUtils

# Pfad zur Revit-Datei
model_path = r"C:\Users\cxs-user\ShareFolder\HDW_ARC_AL.rvt"

# Öffnen des Revit-Dokuments
doc = __revit__.OpenDocumentFile(model_path)

# Überprüfen des Synchronisierungsstatus
needs_sync = WorksharingUtils.IsModelNeedsSynchronization(doc)

if needs_sync:
    print("Das Modell erfordert eine Synchronisierung.")
else:
    print("Das Modell ist auf dem neuesten Stand.")

# Schließen des Dokuments
doc.Close(False)
