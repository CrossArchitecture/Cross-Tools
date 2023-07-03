from pyrevit import revit, DB

def check_sync_status():
    doc = revit.doc
    sync_info = doc.GetWorksharingCentralModelInfo()
    current_user = doc.GetWorksharingCentralUser()

    if current_user:
        # Es gibt bereits einen Benutzer, der synchronisiert
        return True
    else:
        if sync_info.IsWorkshared and sync_info.IsModifiable:
            # Das Modell wird synchronisiert
            return False
        else:
            # Das Modell wird nicht synchronisiert
            return False

def sync_model():
    # Führen Sie hier Ihren Synchronisationscode aus
    doc = revit.doc
    revit.uidoc.SynchronizeWithCentral(DB.TransactWithCentralOptions())

# Überprüfen, ob das Modell synchronisiert wird
if not check_sync_status():
    # Das Modell wird nicht synchronisiert, synchronisieren
    sync_model()
else:
    print("Ein anderer Benutzer synchronisiert das Modell.")