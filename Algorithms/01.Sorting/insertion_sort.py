def insertion_sort(array):
    
    for i in range(1, len(array)):
        insert_index = i
        current_value = array[i]
        
        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                array[j+1] = array[j]
                insert_index = j
            else:
                break
            
        array[insert_index] = current_value
        
    return array



#-------------------------------------------
arr = [3, 7, 8, 5, 1]
print(insertion_sort(arr))