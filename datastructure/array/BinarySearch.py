def search(ar, num):
    l = 0
    r = len(ar) - 1

    while l <= r:
        m = int((r + l)/2)
        if ar[m] < num:
            l = m + 1
        elif ar[m] > num:
            r = m - 1
        else:
            return m

    return -1


def search_recursive(ar, num):
    return find(ar, num, 0, len(ar) - 1)


def find(ar, num, l, r):
    if l > r:
        return -1

    m = int((r + l)/2)
    if ar[m] < num:
        return find(ar, num, m + 1, r)
    elif ar[m] > num:
        return find(ar, num, l, m - 1)
    else:
        return m


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 88, 98, 101]
print(search_recursive(arr, 102))
