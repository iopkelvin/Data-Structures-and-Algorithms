'''
Problem 3: Rearrange Array Digits
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers.
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
'''


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # First check for inputs
    if len(input_list) == 0:
        return []
    # Split > Merge sorted
    digits = merge_sort(input_list)
    # Array is now sorted from max value to min value
    # Separate array by odd and integer indexes
    odd, even = 0, 0
    for index, value in enumerate(digits):
        if index % 2 == 0:
            odd = odd * 10 + value
        else:
            even = even * 10 + value
    return [odd, even]


def merge_sort(arr):
    '''
    Split array to smaller pieces and merge them sorted
    Args:
        arr: List of numbers
    Returns: Two splits of array sorted
    '''
    if len(arr) == 1:
        return arr
    mid_index = len(arr) // 2
    # Split left and right
    left = merge_sort(arr[:mid_index])
    right = merge_sort(arr[mid_index:])
    return merge(left, right)


def merge(left, right):
    '''
    Works along with merge_sort function.
    Takes in two small to large arrays and merges them sorted
    Returns: Single Sorted array
    '''
    left_index = 0
    right_index = 0
    merged_list = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(right[right_index])
            right_index += 1
        else:
            merged_list.append(left[left_index])
            left_index += 1
    # Add leftover
    merged_list += left[left_index:]
    merged_list += right[right_index:]
    return merged_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
    print('Array: ', test_case[0])
    print('Solution: ', test_case[1])
    # print('\n')


if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    # Repeating Numbers
    test_function([[1, 1, 1, 1, 1], [111, 11]])
    test_function([[1, 1, 2, 2, 3, 3, 4, 4], [4321, 4321]])

    # Out of Order
    test_function([[9, 1, 8, 2, 7, 3, 9], [9831, 972]])
    test_function([[3, 0, 4, 6, 2, 5, 9, 8, 7, 1], [97531, 86420]])

    test_function([[], []])
    test_function([[3], [3]])
    test_function([[], [0, 0]])
    test_function([[9], [9, 0]])
