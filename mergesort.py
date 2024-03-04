def mergesort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a

    # Sort
    left = mergesort(a[:len(a)//2])
    right = mergesort(a[len(a)//2:])

    left_num = 0
    right_num = 0
    result = []

    # Add items in sorted order
    while left_num < len(left) and right_num < len(right):
        if left[left_num] < right[right_num]:
            result.append(left[left_num])
            left_num += 1
        else:
            result.append(right[right_num])
            right_num += 1

    # Finish adding the remainder of the left or right lists
    while left_num < len(left):
        result.append(left[left_num])
        left_num += 1

    while right_num < len(right):
        result.append(right[right_num])
        right_num += 1

    return result
