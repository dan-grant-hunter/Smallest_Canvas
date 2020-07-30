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
def all_coordinatess():
    coordinates = []
    for i in range(amount_of_coordinates):
        try:
            coordinate_input = int(input(f"Enter the coordinates for paint splat {i+1}: "))
            if [number for number in coordinate_input.split(",")] not in range(1, 100):
               print('Numbers in coordinates must be between 0 and 100')
               continue
        except ValueError:
            print("Please enter numbers between 0 and 100 seperated by a comma (no spaces)")
            continue
        else:
            coordinates.append(coordinate_input)
            break
    return coordinates



# Calculate the Smallest Canvas Size



# Return the Smallest Canvas Size



# Main Loop
def mainLoop():
    pass


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
