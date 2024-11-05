def calculate_pyramid_height(number_of_blocks):
    if number_of_blocks <= 0:
        raise ValueError("Number of blocks cannot be less than or equal to zero.")

    height = 0
    level = 1

    while level <= number_of_blocks:
        height += 1
        number_of_blocks -= level
        level += 1

    return height
