def maxnum(nums):
    for i in range(len(nums)):
        if nums[i] <= nums[i+1]:
            pass
        else:
            return nums[i]

a = maxnum([10,20,40,70,90,10,8,7,6,5,4])
print(a)