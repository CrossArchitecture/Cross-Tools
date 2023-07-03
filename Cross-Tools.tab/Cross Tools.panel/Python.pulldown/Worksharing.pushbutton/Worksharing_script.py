from pyrevit import revit, DB, UI

def check_sync_status():
    doc = revit.doc
    options = DB.SynchronizeWithCentralOptions()
    options.SetRelinquishOptions(DB.RelinquishOptions(False))

    try:
        doc.SynchronizeWithCentral(options)
        return False
    except DB.SynchronizationWithCentralException as ex:
        if ex.FailureReason == DB.SynchronizationFailureReason.CentralIsNotAvailable:
            return True
        else:
            raise

def sync_model():
    uidoc = revit.uidoc
    uiapp = revit.uiapp
    options = DB.SynchronizeWithCentralOptions()
    options.SetRelinquishOptions(DB.RelinquishOptions(True))

    try:
        uidoc.SynchronizeWithCentral(options, uiapp)
        print("Modell erfolgreich synchronisiert.")
    except DB.SynchronizationWithCentralException as ex:
        print("Fehler beim Synchronisieren des Modells:", ex.Message)

# Überprüfen, ob das Modell synchronisiert wird
if not check_sync_status():
    # Das Modell wird nicht synchronisiert, synchronisieren
    sync_model()
else:
    print("Ein anderer Benutzer synchronisiert das Modell.")
