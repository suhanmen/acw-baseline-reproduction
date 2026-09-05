python
def find_demlo(number):
    n = len(number)
    if n % 2 != 0:
        return None
    first_half = list(map(int, list(number[:n//2])))
    second_half = list(map(int, list(number[n//2:]))[::-1])
    result = []
    for i in range(n//2):
        result.append(str(first_half[i]))
        result.append(str(i+1))
    for i in range(n//2):
        result.append(str(i+1))
        result.append(str(second_half[i]))
    return ''.join(result)