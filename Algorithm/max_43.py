def max(arr):
    maxNum = arr[0]
    for i in arr:
        if i > maxNum:
            maxNum = i
    return maxNum

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 787, 2]
arrr = [1, 2, 3]

print max(arr)


def maxR(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        sub_max = arr[1:]
        return maxR(sub_max)

print maxR(arr)