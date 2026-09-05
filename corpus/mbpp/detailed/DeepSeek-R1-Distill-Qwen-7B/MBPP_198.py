# Test case 1
assert abs(largest_triangle(4, 2) - 10.392304845413264) < 1e-9

# Test case 2
assert abs(largest_triangle(5, 7) - 4.639421805988064) < 1e-9

# Test case 3
assert abs(largest_triangle(9, 1) - 105.2220865598093) < 1e-9

# Test case 4 (invalid input)
try:
    largest_triangle(-3, 4)
except ValueError:
    print("Invalid input caught correctly.")
else:
    print("No exception was thrown for invalid input.")