# https://www.digminecraft.com/getting_started/coordinate_system.php

# How the Coordinate System Works
#
# The Minecraft map is divided into XYZ coordinates. Each of the X, Y and Z values is used to indicate your position in the map.
#
# Here is how the coordinate system works:
#
#     X - Determines your position East/West in the map. A positive value increases your position to the East. A negative value increases your position to the West.
#     Y - Determines your position up/down in the map. A positive value increases your position upward. A negative value increases your position downward.
#     Z - Determines your position South/North in the map. A positive value increases your position to the South. A negative value increases your position to the North.


class Direction:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


NORTH = Direction(0, 0, -1)
SOUTH = Direction(0, 0, 1)
WEST = Direction(-1, 0, 0)
EAST = Direction(1, 0, 0)
UP = Direction(0, 1, 0)
DOWN = Direction(0, -1, 0)
