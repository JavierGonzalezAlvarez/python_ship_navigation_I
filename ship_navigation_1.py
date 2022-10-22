import sys
import math

x = y = 0
initialPosition = (x, y)
initialDirection = "east"
final_coordinates = [(initialPosition, initialDirection)]
options = '''
            ● Action N means to move north by the given value.
            ● Action S means to move south by the given value.
            ● Action E means to move east by the given value.
            ● Action W means to move west by the given value.
            ● Action L means to turn left the given number of degrees.
            ● Action R means to turn right the given number of degrees.
            ● Action F means to move forward by the given value in the direction the ship is
            currently facing.
        '''


def get_distance(x, y) -> int:
    hypotenuse = math.sqrt(x**2 + y**2)
    return hypotenuse


def get_direction(direction, turn) -> str:
    print("current direction and char: ", direction, " - ", turn)
    if direction == "east" and turn == "R":
        new_direction = "south"
    elif direction == "south" and turn == "R":
        new_direction = "west"
    elif direction == "west" and turn == "R":
        new_direction = "north"
    elif direction == "north" and turn == "R":
        new_direction = "east"
    elif direction == "east" and turn == "L":
        new_direction = "north"
    elif direction == "north" and turn == "L":
        new_direction = "west"
    elif direction == "west" and turn == "L":
        new_direction = "south"
    elif direction == "south" and turn == "L":
        new_direction = "east"
    return new_direction


def get_movement(move):
    global initialPosition, initialDirection, final_coordinates, x, y
    final_coordinates = [(initialPosition, initialDirection)]
    key = move[2][0]
    print("final coordinates: ", final_coordinates)
    print("move: ", move)

    position_direction = final_coordinates[-1]
    print("position_direction: ", position_direction)
    position_direction_x = final_coordinates[-1][0][0]
    print("old position_direction_x: ", position_direction_x)
    position_direction_y = final_coordinates[-1][0][1]
    print("old position_direction_y: ", position_direction_y)

    if (key == "R" or key == "L"):
        initialDirection = get_direction(initialDirection, key)
        finalPosition = (position_direction_x, position_direction_y)
        final_coordinates.append(
            {finalPosition, initialDirection})
        # New direction
        initialDirection = initialDirection
        print(initialDirection)

    if initialDirection == "east":
        if (key == "F"):
            addPosition_x = move[2][1]
            print("add position: ", addPosition_x)
            x = int(position_direction_x) + int(addPosition_x)
            print(x)
            finalPosition = (x, y)
            final_coordinates.append(
                {finalPosition, initialDirection})
        elif key == "N":
            addPosition_y = move[2][1]
            print("add position: ", addPosition_y)
            y = int(position_direction_y) + int(addPosition_y)
            print(y)
            finalPosition = (x, y)
            final_coordinates.append(
                {finalPosition, initialDirection})

    if initialDirection == "south":
        if key == "F":
            addPosition_y = move[2][1]
            print("add position: ", addPosition_y)
            y = int(position_direction_y) - int(addPosition_y)
            print(y)
            finalPosition = (x, y)
            final_coordinates.append(
                {finalPosition, initialDirection})

    if initialDirection == "west":
        print("to be parametered")
        finalPosition = (x, y)
        final_coordinates.append(
            {finalPosition, initialDirection})

    if initialDirection == "north":
        print("to be parametered")
        finalPosition = (x, y)
        final_coordinates.append(
            {finalPosition, initialDirection})

    position = finalPosition[0]+abs(finalPosition[1])
    print(position)

    initialPosition = finalPosition
    print(final_coordinates)

    distance = get_distance(finalPosition[0], abs(finalPosition[1]))
    print(
        f"The Manthattan distance bewtween location and ship's starting point is {round(distance,2)} units")


def check_char(first_char) -> bool:
    allowed_chars = ["N", "S", "E", "W", "L", "R",
                     "F", "n", "s", "e", "w", "l", "r", "f"]
    if first_char in allowed_chars:
        if first_char.isalpha():
            print(f"{first_char} is an alphabetic char allowed")
            return True
    else:
        print(f"{first_char} is not an allowed alphabetic char")


def check_value(value) -> bool:
    if value.isnumeric():
        print(f"{value} is a number")
        return True


def separate_movement_and_values(action) -> list:
    n = len(action)
    first_char = action[0]
    value = action[1:n]
    print(first_char.upper(), " - ", value)
    return (check_char(first_char.upper()), check_value(value), (first_char.upper(), value))


def ask_movement():
    action = ""
    while action != "1":
        print(options)
        action = input("pls, enter a new movement (1 = close): ")
        if action == "1":
            print("bye bye!")
            sys.exit()

        move = separate_movement_and_values(action)
        if (move[0] and move[1]) == True:
            get_movement(move)
        else:
            print("it's not a right input")


if __name__ == "__main__":
    ask_movement()
