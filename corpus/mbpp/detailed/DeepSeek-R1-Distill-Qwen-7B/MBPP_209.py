def heap_replace(heap, new_value):
    # Validate the input heap
    if not isinstance(heap, list) or not heap:
        raise ValueError("Invalid heap: not a list or empty")

    # Check if all elements are numbers (int or float)
    for element in heap:
        if not isinstance(element, (int, float)):
            raise ValueError("All elements in the heap must be numbers")

    # Find the smallest element in the heap
    smallest = heap[0]
    for i in range(1, len(heap)):
        if heap[i] < smallest:
            smallest = heap[i]

    # Create a new heap without the smallest element
    new_heap = heap[1:]

    # Insert the new value into the new heap
    new_heap.insert(0, new_value)

    return new_heap