def print_star_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

num_rows = int(5)
print_star_pyramid(num_rows)