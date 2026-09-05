def sum_difference(n):
    sumofsquares = 0
    squareofsum = 0
    for num in range(1, n+1):
        sumofsquares += num * num
        squareofsum += num
    squareofsum = squareofsum ** 2
    return squareofsum - sumofsquares