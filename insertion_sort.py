def insertion_sort(arr):
    
    for i in range(1,len(arr)):

        current = arr[i]

        while i>0 and arr[i-1]>current:
            arr[i] = arr[i-1]
            i = i - 1
            arr[i] = current
    return arr 


if __name__ == "__main__":
    print(insertion_sort([4,3,5,9,8,2,6]))
