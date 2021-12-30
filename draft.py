def bubleSort(nums):
    """冒泡排序"""
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print("s")
print(bubleSort([2, 1, 3, 0]))
