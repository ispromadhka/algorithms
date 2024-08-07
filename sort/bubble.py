# time complexity:O(n^2)
# memmory complexity:O(n)

def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                 arr[i],arr[j] = arr[j],arr[i]
    return arr