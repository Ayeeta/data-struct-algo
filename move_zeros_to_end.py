def move_zeroes_end(arr):
    non_zeroes = [x for x in arr if x != 0]
    zeros = len(arr) - len(non_zeroes)
    return non_zeroes + [0] * zeros

print(move_zeroes_end([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))