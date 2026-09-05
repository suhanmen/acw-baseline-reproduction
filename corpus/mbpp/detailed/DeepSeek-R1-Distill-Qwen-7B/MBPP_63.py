numbers = [num for pair in pairs for num in pair]
max_diff = 0
n = len(numbers)
for i in range(n):
    for j in range(i+1, n):
        diff = abs(numbers[i] - numbers[j])
        if diff > max_diff:
            max_diff = diff