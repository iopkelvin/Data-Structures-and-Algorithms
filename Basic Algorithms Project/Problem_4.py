'''
Problem 4: Dutch National Flag Problem
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal.
For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
'''


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_0_index = 0
    next_2_index = len(input_list) - 1
    current_index = 0

    while current_index < next_2_index + 1:
        current_element = input_list[current_index]

        if current_element == 0:
            input_list[current_index] = input_list[next_0_index]
            input_list[next_0_index] = current_element
            next_0_index += 1
            current_index += 1
        elif current_element == 2:
            input_list[current_index] = input_list[next_2_index]
            input_list[next_2_index] = current_element
            next_2_index -= 1
        else:
            current_index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
    print('Initial Array: ', test_case)
    print('Sorted Array: ', sorted_array)


if __name__ == "__main__":
    test_function([2, 0, 1])
    test_function([1, 0])
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_function([2, 1, 2, 1, 0, 1])
    ## Edge Case
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([])



