from directions import *


class Floor:

    def __init__(self, length, width, direction_length, direction_width, block_type):
        self.length = length
        self.width = width
        self.direction_length = direction_length
        self.direction_width = direction_width
        self.block_type = block_type

    def build(self, builder, position):
        pos_x, pos_y, pos_z = position
        start_x = pos_x
        start_z = pos_z

        if self.direction_length == NORTH:
            start_x = pos_x - self.direction_length
        if self.direction_width == WEST:
            start_z = pos_z - self.direction_width

        for i in range(start_x, self.length):
            for j in range(start_z, self.width):
                builder.add_block((i, pos_y, j), self.block_type)

class Wall:

    def __init__(self, length, height, direction, block_type):
        self.length = length
        self.height = height
        self.direction = direction
        self.block_type = block_type

    def build(self, builder, position):
        pos_x, pos_y, pos_z = position
        start_x = pos_x
        start_z = pos_z

        for i in range(pos_y, self.height):

            if self.direction == NORTH:
                start_x = pos_x - self.direction_length

            if self.direction == SOUTH or self.direction == NORTH:
                for j in range(start_x, self.length):
                    builder.add_block((j, i, pos_z), self.block_type)

            if self.direction == WEST:
                start_z = pos_z - self.direction_width

            if self.direction == SOUTH or self.direction == NORTH:
                for j in range(start_z, self.length):
                    builder.add_block((start_z, i, j), self.block_type)
