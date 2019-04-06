def number_of_rolls(width, length, height, wallpaper_width, wallpaper_length):
    reserve = 0.1
    perimeter = (width * 2) + (length * 2)
    number_of_canvases = round(perimeter / wallpaper_width)
    number_of_canvases_in_roll = wallpaper_length // (height + reserve)
    total_number_of_rolls = round(number_of_canvases / number_of_canvases_in_roll)
    return total_number_of_rolls
