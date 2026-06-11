def display_coordinates(coords):
    if len(coords) != 2:
        return "Invalid coordinates"
    
    x, y = coords
    return f"X Coordinate: {x}, Y Coordinate: {y}"

coordinates = (10, 20)

print(display_coordinates(coordinates))