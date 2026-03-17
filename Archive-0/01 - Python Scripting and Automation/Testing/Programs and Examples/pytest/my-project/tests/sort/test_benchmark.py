import pytest

from src.my_project.sorting_examples import bubble_sort, insertion_sort, quick_sort


# Sorting - Small
@pytest.mark.sort_small
def test_bubble_sort_small(sort_input1, benchmark):
    result = benchmark(bubble_sort, sort_input1)
    assert result == sorted(sort_input1)

@pytest.mark.sort_small
def test_quick_sort_small(sort_input1, benchmark):
    result = benchmark(quick_sort, sort_input1)
    assert result == sorted(sort_input1)

@pytest.mark.sort_small
def test_insertion_sort_small(sort_input1, benchmark):
    result = benchmark(insertion_sort, sort_input1)
    assert result == sorted(sort_input1)


# Sorting - Large
@pytest.mark.sort_large
def test_bubble_sort_large(sort_input2, benchmark):
    result = benchmark(bubble_sort, sort_input2)
    assert result == sorted(sort_input2)

@pytest.mark.sort_large
def test_quick_sort_large(sort_input2, benchmark):
    result = benchmark(quick_sort, sort_input2)
    assert result == sorted(sort_input2)

@pytest.mark.sort_large
def test_insertion_sort_large(sort_input2, benchmark):
    result = benchmark(insertion_sort, sort_input2)
    assert result == sorted(sort_input2)
