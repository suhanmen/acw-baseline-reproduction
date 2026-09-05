class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

def get_Inv_Count(arr):
    if not arr:
        return 0

    # Coordinate compression
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}  # ranks start from 1
    compressed = [rank[v] for v in arr]

    max_rank = max(compressed)
    ft = FenwickTree(max_rank)
    inversion_count = 0

    for num in reversed(compressed):
        inversion_count += ft.query(num - 1)
        ft.update(num, 1)

    return inversion_count