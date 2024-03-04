def mergesort(nums: list[int]) -> list[int]:
    """ Split the list in half, sort each half, then merge the sorted lists together """

    # If we have a list of only one number, then we have a sorted list
    if len(nums) <= 1:
        return nums

    # Split list into two halves
    left_half = nums[:len(nums)//2]
    right_half = nums[len(nums)//2:]

    # Sort each half
    left = mergesort(left_half)
    right = mergesort(right_half)

    # Keep pointers of where we are in each list when merging them together
    left_index = 0
    right_index = 0
    result = []

    # Loop through both lists, adding each item one at a time to the result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add remaining items in left or right lists
    # Left
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    # Right
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result
