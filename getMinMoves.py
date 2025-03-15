def minimum_moves_to_sort(blocks):
    n = len(blocks)
    if n <= 1:
        return 0
    min_index = 0
    max_index = 0
    for i in range(n):
        if blocks[i] < blocks[min_index]:
            min_index = i
        if blocks[i] > blocks[max_index]:
            max_index = i

    moves_to_front = min_index
    moves_to_end = (n - 1 - max_index) if max_index > min_index else (n - 1 - max_index - 1)

    # Total moves
    total_moves = moves_to_front + moves_to_end
    return total_moves

# Example usage:
blocks = [3, 7, 2, 5, 8, 4, 1, 9]
result = minimum_moves_to_sort(blocks)  # Output: 8


print(f"Result: {result}")
