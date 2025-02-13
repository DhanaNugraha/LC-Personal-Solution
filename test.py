def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            print("1",arr)
            arr[j + 1] = arr[j]
            print("2",arr)
            j -= 1
        # disini j udh -1
        arr[j + 1] = key
        print("3",arr)
    return arr


arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))