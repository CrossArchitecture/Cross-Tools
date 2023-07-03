import pyrevit
from pyrevit import revit, DB, forms

# Methode, um den Synchronisationsstatus des Modells abzurufen
def get_sync_status():
    current_user = revit.doc.GetWorksharingCentralModelPath().GetUserVisibleName()
    if current_user:
        return True  # Das Modell wird bereits synchronisiert
    else:
        return False  # Das Modell ist nicht synchronisiert

# Methode, um das Modell zu synchronisieren
def synchronize_model():
    try:
        revit.doc.SynchronizeWithCentral(DB.TransactWithCentralOptions())
        return True  # Erfolgreich synchronisiert
    except Exception as e:
        return str(e)  # Fehler beim Synchronisieren

# Hauptfunktion, um den Button zu erstellen und den Status zu überprüfen
def main():
    sync_status = get_sync_status()
    if sync_status:
        forms.alert("Das Modell wird bereits synchronisiert. Bitte warten Sie.")
    else:
        result = synchronize_model()
        if result == True:
            forms.alert("Das Modell wurde erfolgreich synchronisiert.")
        else:
            forms.alert("Fehler beim Synchronisieren: {}".format(result))

# Button erstellen
pyrevit.pushbutton.command(main)
