# Implement a quicksort algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = quicksort(array)
print("Quicksort sorted array:", sorted_array)