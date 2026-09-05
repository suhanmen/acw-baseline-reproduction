from heapq import heappop, heappush
class Node:
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index
    def __lt__(self, other):
        return self.value < other.value
def find_minimum_range(list):
    high = float('-inf')
    p = (0, float('inf'))
    pq = []
    for i in range(len(list)):
        heappush(pq, Node(list[i][0], i, 0))
        high = max(high, list[i][0])
    while True:
        top = heappop(pq)
        low = top.value
        i = top.list_num
        j = top.index
        if high - low < p[1] - p[0]:
            p = (low, high)
        if j == len(list[i]) - 1:
            return p
        heappush(pq, Node(list[i][j + 1], i, j + 1))
        high = max(high, list[i][j + 1])