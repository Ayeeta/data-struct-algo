#!/bin/python3

import os
import sys

def hourglassSum(arr):
    """Compute the maximum hourglass sum in a 6x6 2D array."""
    max_sum = -float('inf')

    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
            top = sum(arr[i][j:j+3])
            middle = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            current_sum = top + middle + bottom
            max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    # Read input safely and handle environments without OUTPUT_PATH
    output_path = os.environ.get('OUTPUT_PATH', None)
    arr = [list(map(int, input().strip().split())) for _ in range(6)]

    result = hourglassSum(arr)

    if output_path:
        with open(output_path, 'w') as f:
            f.write(str(result) + '\n')
    else:
        print(result)
