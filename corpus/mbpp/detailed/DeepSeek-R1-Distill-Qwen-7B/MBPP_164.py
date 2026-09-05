def areEquivalent(n1, n2):
    # Helper function to calculate the sum of proper divisors of a number
    def sumProperDivisors(num):
        if num <= 0:
            return 0
        if num == 1:
            return 0
        divisorSum = 1  # 1 is a proper divisor for all numbers > 1
        # Check divisors up to the square root of the number
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                if i == num // i:
                    divisorSum += i
                else:
                    divisorSum += i + num // i
        return divisorSum

    # Calculate the sum of proper divisors for both numbers
    sum1 = sumProperDivisors(n1)
    sum2 = sumProperDivisors(n2)

    # Compare the sums and return the result
    return sum1 == sum2

# Example test cases
print(areEquivalent(36, 57))  # Expected output: False
print(areEquivalent(2, 4))    # Expected output: False
print(areEquivalent(23, 47))  # Expected output: True