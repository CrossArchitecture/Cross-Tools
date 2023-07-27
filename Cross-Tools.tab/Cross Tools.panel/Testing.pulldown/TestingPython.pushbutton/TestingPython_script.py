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

with Transaction(doc, __title__) as t:
    t.Start()

    for tag in all_room_tags:
        room = tag.Room
        room_bb = room.get_BoundingBox(doc.ActiveView)
        room_upper_left = XYZ(room_bb.Min.X, room_bb.Max.Y, room_bb.Min.Z)
        move_room_and_tag(tag, room, room_upper_left)

    t.Commit()