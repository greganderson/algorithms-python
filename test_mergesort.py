import random

from mergesort import mergesort


def test_mergesort():
    nums = [i for i in range(1, 11)]
    expected = nums.copy()
    random.shuffle(nums)

    actual = mergesort(nums)
    assert actual == expected