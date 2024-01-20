# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return None

solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2)) 

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))
        
