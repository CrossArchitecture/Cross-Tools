# -*- coding: utf-8 -*-
__title__   = "Center Room Tags"


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝
#==================================================
from Autodesk.Revit.DB import *

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
#==================================================
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Application

# ELEMENTS
all_room_tags = FilteredElementCollector(doc, doc.ActiveView.Id)\
    .OfCategory(BuiltInCategory.OST_RoomTags).WhereElementIsNotElementType().ToElements()

# CONTROLS
step = 2 # INTERNAL UNITS IN FEET


OFFSET_DISTANCE_FEET = 1.64042  # Offset distance in feet

def move_room_and_tag(tag, room, new_pt):
    """Function to move both Room and Tag Locations, if they are not part of the group.
    :param tag:     Room Tag
    :param room:    Room
    :param new_pt:  XYZ Point."""
    if room.GroupId == ElementId(-1):  # ElementId(-1) means None
        room.Location.Point = new_pt

    if tag.GroupId == ElementId(-1):
        tag.Location.Point = new_pt


# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
#==================================================

def get_corner_choice():
    prompt = "Select the corner for placing the room tags:"
    options = ["Upper Left", "Upper Right", "Lower Left", "Lower Right"]
    dialog = TaskDialog("Corner Choice")
    dialog.MainInstruction = prompt
    for option in options:
        dialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, option)

    result = dialog.Show()

    if result == TaskDialogResult.CommandLink1:
        return TaskDialogResult.CommandLink1
    elif result == TaskDialogResult.CommandLink2:
        return TaskDialogResult.CommandLink2
    elif result == TaskDialogResult.CommandLink3:
        return TaskDialogResult.CommandLink3
    elif result == TaskDialogResult.CommandLink4:
        return TaskDialogResult.CommandLink4
    else:
        # Default to Upper Left or for any other invalid input
        return TaskDialogResult.CommandLink1

with Transaction(doc, __title__) as t:
    t.Start()

    corner_choice = get_corner_choice()

    for tag in all_room_tags:
        room = tag.Room
        room_bb = room.get_BoundingBox(doc.ActiveView)

        if corner_choice == TaskDialogResult.CommandLink1:  # Upper Left
            offset_distance = XYZ(OFFSET_DISTANCE_FEET, -OFFSET_DISTANCE_FEET, 0)
            corner_point = XYZ(room_bb.Min.X, room_bb.Max.Y, room_bb.Min.Z)

        elif corner_choice == TaskDialogResult.CommandLink2:  # Upper Right
            offset_distance = XYZ(-OFFSET_DISTANCE_FEET, -OFFSET_DISTANCE_FEET, 0)
            corner_point = XYZ(room_bb.Max.X, room_bb.Max.Y, room_bb.Min.Z)

        elif corner_choice == TaskDialogResult.CommandLink3:  # Lower Left
            offset_distance = XYZ(OFFSET_DISTANCE_FEET, OFFSET_DISTANCE_FEET, 0)
            corner_point = XYZ(room_bb.Min.X, room_bb.Min.Y, room_bb.Min.Z)

        elif corner_choice == TaskDialogResult.CommandLink4:  # Lower Right
            offset_distance = XYZ(-OFFSET_DISTANCE_FEET, OFFSET_DISTANCE_FEET, 0)
            corner_point = XYZ(room_bb.Max.X, room_bb.Min.Y, room_bb.Min.Z)

        else:  # Default to Upper Left or for any other invalid input
            offset_distance = XYZ(OFFSET_DISTANCE_FEET, -OFFSET_DISTANCE_FEET, 0)
            corner_point = XYZ(room_bb.Min.X, room_bb.Max.Y, room_bb.Min.Z)

        room_corner_with_offset = corner_point + offset_distance
        move_room_and_tag(tag, room, room_corner_with_offset)

    t.Commit()