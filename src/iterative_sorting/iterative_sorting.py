# TO-DO: Complete the selection_sort() function below 
array = [ 0, 1, 5, 7, 8, 3, 2]
def selection_sort( arr ):

    for i in range(0, len(arr)):
        current = arr[i]
        j = i

        while j > 0 and arr[j - 1] > current:
            arr[j] = arr[j - 1]
            j -= 1
    
        arr[j] = current

    print(arr)
    return arr

selection_sort(array)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr