# Reversal algorithm for Array rotation
# Input:
# arr[] = {3, 4, 5, 6, 7, 1, 2}, d = 2
# Output: 1 2 3 4 5 6 7

def rotate_array(arr, d):
    # simple but worst space complexity
    # print(arr[len(arr) - d:] + arr[:len(arr) - d])

    size = len(arr)
    for times in range(d):
        temp = arr[-1]
        # move each element a step backward
        index = size - 2
        while index > 0:
            arr[index + 1] = arr[index]
            index -= 1
        arr[0] = temp


if __name__ == '__main__':
    arr1 = [3, 4, 5, 6, 7, 1, 2]
    rotate_array(arr1, 3)
    print(arr1)
