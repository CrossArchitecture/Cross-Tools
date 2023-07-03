from pyrevit import revit, DB

def check_sync_status():
    doc = revit.doc
    sync_info = doc.GetWorksharingCentralModelInfo()

    if sync_info.IsWorkshared and sync_info.IsModifiable:
        # Das Modell wird synchronisiert
        return True
    else:
        # Das Modell wird nicht synchronisiert
        return False

def sync_model():
    # Führen Sie hier Ihren Synchronisationscode aus
    doc = revit.doc
    current_user = doc.GetWorksharingCentralUser()

    if current_user:
        # Es gibt bereits einen Benutzer, der synchronisiert
        print("Ein anderer Benutzer synchronisiert das Modell.")
    else:
        # Kein anderer Benutzer synchronisiert
        # Führen Sie den Synchronisationscode aus
        revit.uidoc.SynchronizeWithCentral(DB.TransactWithCentralOptions())

# Überprüfen, ob das Modell synchronisiert wird
if not check_sync_status():
    # Das Modell wird nicht synchronisiert, synchronisieren
    sync_model()
else:
    print("Ein anderer Benutzer synchronisiert das Modell.")
