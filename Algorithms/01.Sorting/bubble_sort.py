def bubble_sort(array):
    
    for n in range(len(array)-1, 0, -1):
        for j in range(n):
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array




#------------------------------------------------------------
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)