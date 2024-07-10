def QuickSort(arr, left, right):
    if left > right:
        return
    
    pivot = _partition(arr, left, right)
    
    QuickSort(arr, left, pivot - 1)
    QuickSort(arr, pivot + 1, right)
    

def _partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right
    
    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
            
        if i > j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[left], arr[j] = arr[j], arr[left]

    return j
    