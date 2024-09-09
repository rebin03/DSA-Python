def power_sum(array,power=1):
    
    total = 0
    
    for i in array:
        
        if type(i) == list:
            total += power_sum(i, power+1)
        else:
            total += i
    
    return total**power

print(power_sum([1,2,[3,4],[[2]]]))