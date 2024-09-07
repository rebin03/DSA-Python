def sortedSquares(nums):
    if nums == []:
        return nums
    
    p1, p2 = 0, len(nums)-1
    res = [0]*len(nums)

    for i in range(len(nums)-1, -1, -1):
        sqr1 = nums[p1]**2
        sqr2 = nums[p2]**2

        if sqr1 > sqr2:
            res[i] = sqr1
            p1 += 1
        else:
            res[i] = sqr2
            p2 -= 1

    return res