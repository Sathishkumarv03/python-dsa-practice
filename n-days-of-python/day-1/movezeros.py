"""
Day 1 - Move Zeros to End
----------------------------------
Problem:
Move all zeros in the array to the end while
maintaining the order of non-zero elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# -----------------------------
# Method 1: Two Traversals
# -----------------------------
def move_zeros_two_pass(arr, n):
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1

    while j < n:
        arr[j] = 0
        j += 1


# -----------------------------
# Method 2: Single Traversal (Swap Method)
# -----------------------------
def move_zeros_single_pass(arr, n):
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    # Choose method here:
    move_zeros_two_pass(arr, n)
    # move_zeros_single_pass(arr, n)

    print(*arr)
