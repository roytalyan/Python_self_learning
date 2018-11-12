# coding:utf-8

def bubble(arr):
    count = len(arr)
    for i in range(0, count):
        for j in range(i+1, count):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print arr
    return arr

list = [3,4,1,9,1,2,7,6,54,23,13]

print bubble(list)