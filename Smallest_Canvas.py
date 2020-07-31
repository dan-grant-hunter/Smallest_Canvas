# -----------------------------------------------------------------------------
# Smallest Canvas
# -----------------------------------------------------------------------------

# Get Input for Number of Coordinates
def number_of_coordinates():
    while True:
        try:
            amount_of_coordinates = int(input("Enter the number of paint splats: "))
            if amount_of_coordinates not in range(2, 101):
               print('Number must be between 2 and 100 inclusive')
               continue
        except ValueError:
            print("Please enter a number between 2 and 100 inclusive")
            continue
        else:
            return amount_of_coordinates
            break


# Get Input for all Coordinates
def all_coordinatess(num_of_coords):
    xcoordinates = []
    ycoordinates = []
    for i in range(num_of_coords):
        try:
            coordinate_input = int(input(f"Enter the coordinates for paint splat {i+1}: "))
            x = int(coordinate_input.split(",")[0])
            y = int(coordinate_input.split(",")[1])
            if x not in range(1, 100) or y not in range(1, 100):
                print('Both numbers in coordinates must be between 0 and 100')
                continue
        except ValueError:
            print("Please enter numbers between 0 and 100 seperated by a comma (no spaces)")
            continue
        else:
            xcoordinates.append(x)
            ycoordinates.append(y)
            break
    return xcoordinates, ycoordinates



# Calculate the Bottom Left Coordinates
def smallest_canvas_bottom_left(coordinates):
    smallestx = 0
    smallesty = 0
    for x, y in coordinates:
        if not smallestx or x < smallestx:
            smallestx = x
        if not smallesty or y < smallesty:
            smallesty = y
    smallest = ((smallestx - 1), (smallesty - 1))
    return ','.join([str(num) for num in smallest])


# Calculate the Top Right Coordinates
def smallest_canvas_top_right(coordinates):
    smallestx = 0
    smallesty = 0
    for x, y in coordinates:
        if not smallestx or x > smallestx:
            smallestx = x
        if not smallesty or y > smallesty:
            smallesty = y
    smallest = ((smallestx + 1), (smallesty + 1))
    return ','.join([str(num) for num in smallest])


# Main Loop
def mainLoop():
    num_of_coords = number_of_coordinates()
    coordinates = all_coordinatess(num_of_coords)
    print(smallest_canvas_bottom_left(coordinates))
    print(smallest_canvas_top_right(coordinates))


# Replay Prompt
if __name__ == '__main__':
    while True:
        mainLoop()
        while True:
            answer = input('Calculate Again? (Y/N): ')
            if answer.upper() in ('Y', 'N'):
                break
            print('\nInvalid input\n')
        if answer.upper() == 'Y':
            continue
        else:
            break
