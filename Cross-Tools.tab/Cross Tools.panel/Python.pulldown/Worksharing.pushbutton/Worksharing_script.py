import clr
clr.AddReference('RevitAPI')
import Autodesk.Revit.DB as DB

# Pfad zur Revit-Datei
model_path = "C:\Users\cxs-user\ShareFolder\HDW_ARC_AL.rvt"

# Öffnen des Revit-Dokuments
doc = DB.Document.Open(model_path)

# Überprüfen des Synchronisierungsstatus
needs_sync = doc.IsModelNeedsSynchronization()

if needs_sync:
    print("Das Modell erfordert eine Synchronisierung.")
else:
    print("Das Modell ist auf dem neuesten Stand.")

# Schließen des Dokuments
doc.Close()
