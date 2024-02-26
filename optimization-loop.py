def largest(lst: list[int]) -> int:
    """
    Finds the largest number in the list, returning None if the list is empty

    :param lst: List of numbers
    :return: Largest number in the list, or None if the list is empty
    """
    if len(lst) == 0:
        return None

    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    
    return largest


def main():
    test = [1, 3, 7, 5, 3, 3, 12, 5, 7, 5, 3, 10, 9, 9]

    print(largest(test))


if __name__ == "__main__":
    main()