# Program for array rotation
# Input:
# arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2
#
# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
# Output: 5 6 7 1 2 3 4


def rotate_array(arr, d):
    # simple but worst space complexity
    # print(arr[d:] + arr[:d])

    size = len(arr)
    for times in range(d):
        temp = arr[0]
        # move each element a step forward
        index = 0
        while index < size - 1:
            arr[index] = arr[index + 1]
            index += 1
        arr[-1] = temp


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(arr1, 2)
    print(arr1)
