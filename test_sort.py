import pytest

from main import merge_sort
from oop_merge import MergeSort

def test_sort():
    array = [1,5,3,90,2]
    merge_sort(array)
    assert array == [1,2,3,5,90]

def test_oop_sort():
    array = MergeSort([1,4,38,9, 0, 45, 73])
    assert array.arr == [0,1,4,9,38,45,73]

def test_oop_sort_2():
    new_arr = MergeSort([1,2,78, 4, 0, 2])
    assert new_arr.arr == [0,1,2,2,4,78]