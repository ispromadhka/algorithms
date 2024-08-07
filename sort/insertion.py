# time complexity:O(n) -> O(n^2)
# memmory complexity:O(n)

def insertion_sort(arr:list) -> list:
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]
    return arr
