'''
Problem 1: Square Root of an Integer

Finding the Square Root of an Integer
Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
'''


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print("Can't get square root of a negative number")
    if number == 0 or number == 1:
        return number
    return sqrt_recursive(0, number, number)


def sqrt_recursive(low, high, number):
    if low > high:
        return high
    middle = (low + high) // 2
    middle_squared = middle * middle
    if middle_squared == number:
        return middle
    elif middle_squared > number:
        return sqrt_recursive(low, middle-1, number)
    else:
        return sqrt_recursive(middle+1, high, number)


def print_sqrt(number, sqrt_n):
    if (number >= 0) and (sqrt_n >= 0):
        print("The (floor value) square root of {} is {}".format(number, sqrt_n))
        print("Pass" if (sqrt_n == sqrt(number)) else "Fail")
    else:
        print('The (floor value) square root of {} is: '.format(number))
        print(sqrt(number))
    return


if __name__ == "__main__":
    print_sqrt(9, 3)
    print_sqrt(0, 0)
    print_sqrt(16, 4)
    print_sqrt(1, 1)
    print_sqrt(27, 5)
    print_sqrt(-1, 1)


