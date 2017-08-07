nums = [10, 80, 30, 90, 40, 50, 70]

print nums[-1]


def partition(arr, left, right):
    pivot = arr[right]
    j = left
    for k in range(left, right):
        if arr[k] <= pivot:
            nums[k], nums[j] = nums[j], nums[k]
            j += 1
    arr[j], arr[right] = arr[right], arr[j]
    return j


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quickSort(arr, left, pi - 1)
        quickSort(arr, pi + 1, right)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" % arr[i]),
