import random

from mergesort import mergesort


def test_mergesort():

    # Random ordered list of numbers from 1-10
    a = [i for i in range(1, 11)]
    random.shuffle(a)

    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    actual = mergesort(a)
    assert actual == expected
