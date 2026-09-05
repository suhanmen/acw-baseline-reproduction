def dog_age(human_years):
    if not isinstance(human_years, int):
        raise ValueError("human_years must be an integer")
    if human_years < 1:
        raise ValueError("human_years must be at least 1")

    if human_years == 1:
        return 15
    elif human_years == 2:
        return 24
    else:
        base_dog_years = 24  # from first two years
        remaining_years = human_years - 2
        dog_years = base_dog_years + (remaining_years * 4)
        # Subtract 1 dog year for every 3 additional human years
        dog_years -= remaining_years // 3
        return dog_years

# Test the function with the given assertions
assert dog_age(12) == 61
assert dog_age(15) == 73
assert dog_age(24) == 109

# Additional tests
print(dog_age(1))   # Expected 15
print(dog_age(2))   # Expected 24
print(dog_age(3))   # Expected 28 (24 + 4)
print(dog_age(6))   # Expected 39 (24 + 16 - 1)