def twoSum(nums, target):
    for t1, n1 in enumerate(nums):
        for t2, n2 in enumerate(nums):
            if t1 == t2:
                continue
            elif n1 + n2 == target:
                return [t1, t2]
                break

