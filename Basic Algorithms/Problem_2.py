'''
Problem 2: Search in a Rotated Sorted Array
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
'''


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(list): Input array to search
       number(int): Target to search for
    Returns:
       int: Index or -1
    """
    return binary_search_recursive(input_list, number, 0, len(input_list) - 1)


def binary_search_recursive(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]
    if target == mid_element:
        return mid_index
    # Search left side of array
    index_left_side = binary_search_recursive(array, target, start_index, mid_index - 1)
    # Search right side of array
    index_right_side = binary_search_recursive(array, target, mid_index + 1, end_index)
    # Inevitably either index_left_side or index_right_side will be -1, so the one that finds number is returned
    if index_left_side > index_right_side:
        return index_left_side
    return index_right_side


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

    print("Array:", input_list)
    print("Number:", number)
    print("linear Search:", linear_search(input_list, number))
    print("Rotated Array Search: ", rotated_array_search(input_list, number))
    print()


if __name__ == "__main__":
    # Rotated array
    print('------Rotated arrays------')
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 7])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 1, 2, 3, 4], 7])
    test_function([[6, 7, 1, 2, 3, 4], 1])
    test_function([[6, 7, 1, 2, 3, 4], 3])

    # Non-rotated array
    print('------Non-rotated array------')
    test_function([[0, 1, 2, 3, 4, 5, 6], 5])
    test_function([[1, 3, 5, 7, 9, 11, 13], 3])

    # Non-Present
    print('------Non-present number------')
    test_function([[1], 0])

    # Empty array
    print('------Empty array------')
    test_function([[], 5])

    # 1 element array
    print('------One element array present------')
    test_function([[5], 5])

    # Random
    test_function([[7, 5, 3, 1, 9, 11, 13], 11])
    test_function([[7, 3, 5, 8, 2, 14, 11, 1], 14])