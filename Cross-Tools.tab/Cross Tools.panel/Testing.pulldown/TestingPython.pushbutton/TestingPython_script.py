# ... (Previous code remains the same)

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
#==================================================

with Transaction(doc, __title__) as t:
    t.Start()

    for tag in all_room_tags:
        # ROOM DATA
        room = tag.Room
        room_bb = room.get_BoundingBox(doc.ActiveView)
        room_min = room_bb.Min

        # MOVE TO UPPER-LEFT CORNER (if possible)
        if room.IsPointInRoom(room_min):
            move_room_and_tag(tag, room, room_min)

        # FIND ANOTHER LOCATION
        else:
            room_boundaries = room.GetBoundarySegments(SpatialElementBoundaryOptions())
            room_segments   = room_boundaries[0]

            # Get Longest Segment
            length = 0
            longest_curve = None

            for seg in room_segments:
                curve = seg.GetCurve()
                if curve.Length > length:
                    longest_curve = curve
                    length = curve.Length

            # Get upper-left corner point of the Bounding Box
            pt_upper_left = XYZ(room_bb.Min.X, room_bb.Max.Y, room_bb.Min.Z)

            # Move the tag to the upper-left corner point if it is inside the room boundaries
            if room.IsPointInRoom(pt_upper_left):
                move_room_and_tag(tag, room, pt_upper_left)

    t.Commit()
