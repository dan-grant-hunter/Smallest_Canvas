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
def all_coordinates(num_of_coords):
    xcoordinates = []
    ycoordinates = []
    for i in range(num_of_coords):
        while True:
            try:
                coordinate_input = input(f"Enter the coordinates for paint splat {i+1}: ")
                x = int(coordinate_input.split(",")[0])
                y = int(coordinate_input.split(",")[1])
                if x not in range(1, 100) or y not in range(1, 100):
                    print('Both numbers in coordinates must be between 0 and 100')
                    continue
            except (ValueError, IndexError):
                print("Please enter numbers between 0 and 100 seperated by a comma (no spaces)")
                continue
            else:
                xcoordinates.append(x)
                ycoordinates.append(y)
                break
    return xcoordinates, ycoordinates


# Calculate the Smallest Canvas Size
def smallest_canvas(coordinates):
    smallestx_for_bl = min(coordinates[0])
    smallesty_for_bl = min(coordinates[1])
    smallestx_for_tr = max(coordinates[0])
    smallesty_for_tr = max(coordinates[1])
    smallest_bl = ((smallestx_for_bl - 1), (smallesty_for_bl - 1))
    smallest_tr = ((smallestx_for_tr + 1), (smallesty_for_tr + 1))
    print(','.join([str(num) for num in smallest_bl]))
    print(','.join([str(num) for num in smallest_tr]))


# Main Loop
def mainLoop():
    num_of_coords = number_of_coordinates()
    coordinates = all_coordinates(num_of_coords)
    smallest_canvas(coordinates)


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
