# Double iterate solution.
# def twoSum(nums, target):
#     numLen = len(nums)
#     for idx1 in list(range(nums)):
#         for idx2 in list(range(idx1+1,nums)):
#             if nums[idx1] + nums[idx2] == target:
#                 resultList = [idx1, idx2]
#     return resultList

# Directory solution.
def twoSum(nums, target):
    numLen = len(nums)
    numDic = {}
    resultList = []
    for i in range(numLen):
        numDic[nums[i]] = i
    for i in range(numLen):
        complement = target - nums[i]
        print(complement)
        if complement in numDic.keys() and numDic[complement] != i:
            resultList = [i, numDic[complement]]
    return resultList

print(twoSum([3,3], 6))