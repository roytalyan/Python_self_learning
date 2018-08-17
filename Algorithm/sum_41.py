def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print sum(arr)

def sumRcursion(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])



print sumRcursion(arr)