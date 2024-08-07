# time complexity:O(nlog(n)
# memmory complexity:O(log(n)) -> O(n)

def quick_sort(arr:list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        more = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)
