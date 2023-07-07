def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    less = [i for i in arr if i < pivot]
    greate = [j for j in arr if j > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greate)
