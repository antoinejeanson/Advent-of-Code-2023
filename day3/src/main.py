from enum import Enum

class DataTypes:
    EMPTY = 0
    PART_NUMBER = 1
    PART = 2

with open('input.txt') as f:
    data = f.readlines()

# Interpret data
interpreted_data = []

for y, line in enumerate(data):
    interpreted_line = []
    for x, character in enumerate(line):

        if character == ".":
            interpreted_line.append(DataTypes.EMPTY)
        elif character.isnumeric():
            interpreted_line.append(DataTypes.PART_NUMBER)
        else:
            interpreted_line.append(DataTypes.PART)

    interpreted_data.append(interpreted_line)

print(interpreted_data)
