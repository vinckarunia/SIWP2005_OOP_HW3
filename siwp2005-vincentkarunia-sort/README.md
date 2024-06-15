# Sorting Algorithms

This package provides a collection of sorting algorithms implemented in Python. The following sorting algorithms are included:

- Bubble Sort
- Insertion Sort
- Quick Sort

## Installation

You can install the package using pip:

```sh
pip install -i https://test.pypi.org/simple/ siwp2005-vincentkarunia-sort==0.0.2
```

## Usage

Here is an example of how to use the sorting algorithms:

```python
from sort.src import bubble_sort, insertion_sort, quick_sort

numbers = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort
sorted_numbers = bubble_sort(numbers)
print(f'Bubble Sorted: {sorted_numbers}')

# Insertion Sort
sorted_numbers = insertion_sort(numbers)
print(f'Insertion Sorted: {sorted_numbers}')

# Quick Sort
sorted_numbers = quick_sort(numbers)
print(f'Quick Sorted: {sorted_numbers}')
```

## Algorithms

### Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### Insertion Sort
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms.

### Quick Sort
Quick Sort is an efficient sorting algorithm that uses a divide-and-conquer strategy to quickly sort elements in a list.

## License

This project is licensed under the MIT License.