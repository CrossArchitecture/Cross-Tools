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


def move_room_and_tag_to_upper_left(tag, room):
    """Function to move both Room and Tag Locations to the upper-left corner of the room,
    if they are not part of the group.
    :param tag:     Room Tag
    :param room:    Room"""
    if room.GroupId == ElementId(-1):  # ElementId(-1) means None
        room_bb = room.get_BoundingBox(doc.ActiveView)
        room_upper_left = XYZ(room_bb.Min.X, room_bb.Max.Y, room_bb.Min.Z)
        tag.Location.Point = room_upper_left

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
#==================================================

with Transaction(doc, __title__) as t:
    t.Start()

    for tag in all_room_tags:
        room = tag.Room
        move_room_and_tag_to_upper_left(tag, room)

    t.Commit()