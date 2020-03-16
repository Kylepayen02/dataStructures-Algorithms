def binary_search(lst, low, high):
    high=len(lst)
    while (low <= high):
        mid = int((low + high) / 2)
        if (lst[mid] == 1 and (mid == 0 or lst[mid - 1] == 0)):
            return mid
        elif (lst[mid] == 1):
            high = mid - 1
        else:
            low = mid + 1


def findChange(lst01):
    value = binary_search(lst01, 0, 1)
    return (value)

