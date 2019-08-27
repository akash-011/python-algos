def binary_search(arr, lower, upper, x):

    while lower <= upper:

        mid = lower + (upper - lower) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            lower = mid + 1

        else:
            upper = mid - 1

    return -1


# Test Case , Expected result = 1
arr = [1, 2, 3, 4, 5, 6]
result = binary_search(arr, 0, len(arr) - 1, 2)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not found in array")
