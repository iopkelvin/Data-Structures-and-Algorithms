'''
Problem 6: Unsorted Integer Array
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
'''

def get_min_max(array):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(array) == 0:
        return None
    min_val = array[0]
    max_val = array[0]

    for value in array:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return (min_val, max_val)


def print_test(answer, array):
    print("Pass" if (answer == get_min_max(array)) else "Fail")
    print('Unsorted Array: ', array)
    print('(min, max): ', get_min_max(array))
    return

'''
Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
'''
if __name__ == "__main__":
    import random
    ## Example Test Case of Ten Integers
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    result = (0,9)
    # Test 1
    random.shuffle(l)
    print_test(result ,l)
    # Test 2
    random.shuffle(l)
    print_test(result, l)

    ## Example Test Case of Twenty Integers
    l = [i for i in range(0, 20)]  # a list containing 0 - 9
    result = (0, 19)
    # Test 3
    random.shuffle(l)
    print_test(result, l)
    # Test 4
    random.shuffle(l)
    print_test(result, l)

    ## Example Test Case of no Integers
    l = [i for i in range(0)]
    result = None
    # Test 5
    # random.shuffle(l)
    print_test(result, l)

    ## Example Test Case including negative integers
    l = [i for i in range(-20, 0)]  # a list containing 0 - 9
    result = (-20, -1)
    # Test 6
    random.shuffle(l)
    print_test(result, l)

    ## Example Test Case including negative and positive integers
    l = [i for i in range(-20, 20)]  # a list containing 0 - 9
    result = (-20, 19)
    # Test 7
    random.shuffle(l)
    print_test(result, l)
