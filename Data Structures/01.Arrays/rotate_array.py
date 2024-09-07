# function to rotate an array using two pointers
def reverse(array,start,end):
    
    while(start<end):
        array[start],array[end] = array[end], array[start]
        start +=1
        end -=1
        
    return array

def rotate_array(array,k):
    
    if len(array) == 0: return []
    k= k % len(array)

    reverse(array, 0, len(array)-1) # [5, 4, 3, 2, 1] - rotating the entire array
    reverse(array, 0, k-1)          # [4, 5, 3, 2, 1] - rotating the first k element from the rotated array
    reverse(array, k, len(array)-1) # [4, 5, 1, 2, 3] - output, rotated array of k times
    
    return array

print(rotate_array([1,2,3,4,5],3))
