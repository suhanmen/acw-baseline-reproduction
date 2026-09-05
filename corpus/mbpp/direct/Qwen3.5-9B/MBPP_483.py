def first_Factorial_Divisible_Number(x: int) -> int:
    if x <= 0:
        raise ValueError("x must be a positive integer")

    n = 1
    factorial = 1

    while True:
        if factorial % x == 0:
            return n

        n += 1
        factorial *= n


if __name__ == "__main__":
    import sys

    def run_tests():
        assert first_Factorial_Divisible_Number(10) == 5
        assert first_Factorial_Divisible_Number(15) == 5
        assert first_Factorial_Divisible_Number(5) == 4
        print("All tests passed.")

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        # Example usage
        try:
            val = int(input("Enter a positive integer x: "))
            result = first_Factorial_Divisible_Number(val)
            print(f"The first natural number whose factorial is divisible by {val} is: {result}")
        except Exception as e:
            print(f"Error: {e}")