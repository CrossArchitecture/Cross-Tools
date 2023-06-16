# -*- coding: utf-8 -*-

__title__ = "Place Views on Sheets"   # Name of the button displayed in Revit
__author__ = "Erich Domme"
# __context__ = 'Views'
__doc__ = """Description:
>>> THIS TOOL IS STILL WORK IN PROGRESS <<<

Place selected views on new sheets.
_____________________________________________________________________
How-to:

-> Select views in ProjectBrowser
-> Click the button
-> Select TitleBlock
-> Set SheetNumbering rules
-> Run
"""

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTS
import sys
from pyrevit import forms
from Autodesk.Revit.DB import (BuiltInParameter,
                               Transaction,
                               ViewSheet,
                               Viewport,
                               XYZ)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CUSTOM IMPORTS
from Snippets._selection import get_selected_views, select_title_block

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> VARIABLES
doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI
# TODO
class MyWindow(forms.WPFWindow):
    """GUI for View renaming tool."""
    def __init__(self, xaml_file_name):
        self.form = forms.WPFWindow.__init__(self, xaml_file_name)

    #>>>>>>>>>> PROPERTIES
    @property
    def prefix(self):
        return self.field_prefix.Text

    @property
    def start_count(self):
        return int(self.field_start_count.Text)

    @property
    def origin_x(self):
        return float(self.field_origin_x.Text)

    @property
    def origin_y(self):
        return float(self.field_origin_y.Text)

    @property
    def origin_z(self):
        return float(self.field_origin_z.Text)

    #>>>>>>>>>> GUI EVENTS
    def buttonclick_run(self, sender, e):
        """Button action: Rename view with given """
        # create_sheets(self.n_copies, self.prefix, self.start_count)
        self.Close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MAIN
if __name__ == '__main__':

    #>>>>>>>>>> GET SELECTED VIEWS
    selected_views = get_selected_views(uidoc)
    if not selected_views:
        forms.alert("No views selected. Please try again.", exitscript=True)

    #>>>>>>>>>> FILTER VIEWS ALREADY ON SHEETS
    selected_views_already_on_sheet = [view for view in selected_views if view.get_Parameter(BuiltInParameter.VIEWER_SHEET_NUMBER).AsString() != '---']
    selected_views = [view for view in selected_views if view.get_Parameter(BuiltInParameter.VIEWER_SHEET_NUMBER).AsString() == '---']

    #>>>>>>>>>> PRINT VIEWS NOT ON SHEETS
    # fixme add equal spacing
    if selected_views_already_on_sheet:
        print("="*30 + " Views that are already placed on sheets:")
        for view in selected_views_already_on_sheet:
            print('View [{}] - Sheet [{}]'.format(view.Name, view.get_Parameter(BuiltInParameter.VIEWER_SHEET_NUMBER).AsString()))

    #>>>>>>>>>> SELECT TITLEBLOCK
    selected_title_block = select_title_block(uidoc, exitscript=True)

    #>>>>>>>>>> OPEN GUI
    GUI = MyWindow("Script.xaml")
    GUI.ShowDialog()

    prefix = GUI.prefix
    start_count = GUI.start_count
    origin_x = GUI.origin_x
    origin_y = GUI.origin_y
    origin_z = GUI.origin_z

    #>>>>>>>>>> MAIN LOOP
    print("="*30 + " Placing {} views on sheets.".format(len(selected_views)))

    t = Transaction(doc, "Py: New Sheets")
    t.Start()

    for view in selected_views:
        #>>>>>>>>>> CREATE SHEET
        Sheet = ViewSheet.Create(doc, selected_title_block)

        #>>>>>>>>>> SET SHEET NUMBER
        count = "{:02d}".format(start_count)  # 1 -> 01...
        sheet_number = prefix + count

        fail_count = 0
        while True:
            fail_count += 1
            if fail_count > 10:
                break
            try:
                Sheet.SheetNumber = sheet_number
                break
            except:
                sheet_number += "*"
        start_count += 1

        #>>>>>>>>>> PLACE VIEW ON SHEET
        Viewport.Create(doc, Sheet.Id, view.Id, XYZ(origin_x, origin_y, origin_z))
        Sheet.Name = view.Name
        print('Created sheet: {} - {}'.format(sheet_number, Sheet.Name))

    t.Commit()
