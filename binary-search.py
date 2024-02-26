def binary_search(lst: list[int], target: int) -> int:
    """
    Performs a binary search on a list of numbers, returning the index of the element
     if it exists, -1 if it does not.
     
     :param lst: List of integers in ascending sorted order
     :param target: The integer we are looking for
     :return: The index of the target integer, -1 if it cannot be found
     """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2 # Find middle element

        if lst[mid] == target:
            return mid # Target acquired
        elif lst[mid] < target:
            left = mid + 1 # Target not in left half of list, check the right side
        else:
            right = mid - 1 # Target not in right half of list, check the left side
    
    return -1 # Target not in list


def main():
    test = [i for i in range(100)]

    # The index should just be the number in the test since the list is 0-99
    # This wouldn't be the case in a different sorted list
    print(binary_search(test, 50))
    print(binary_search(test, 20))
    print(binary_search(test, 76))
    print(binary_search(test, 1))
    print(binary_search(test, 99))
    print(binary_search(test, 124)) # -1
    print(binary_search(test, -13)) # -1


if __name__ == "__main__":
    main()