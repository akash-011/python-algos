def selection_sort(arr):

    for i in range(len(arr)):

        minPosition = i

        for j in range(i+1, len(arr)):
            if arr[minPosition] > arr[j]:
                minPosition = j
        
        temp = arr[i]
        arr[i] = arr[minPosition]
        arr[minPosition] = temp
    
    return arr
