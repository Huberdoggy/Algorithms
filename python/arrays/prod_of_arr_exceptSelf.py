"""
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time
and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if not nums:
            return (answer := [0])
        elif len(nums) >= 1 and len(nums) <= 2:
            # Eval and return the literal equivalent of 'answer[i]' or
            # 'answer[1]' multiplied by 'answer[0]'
            return (
                answer := [x * 1 for x in nums[1::-1]] if len(nums) == 2 else [nums[0]]
            )
        else:
            answer = [0 * x for x in range(len(nums))]
            answer[0] = 1  # Will multiply first element by 1
            # since there's nothing to look back to the left
            for i in range(1, len(nums)):
                # For each 'i' from index 1 onward, our 'answer[i]' equals
                # product of prev 'answer' and prev input array
                answer[i] = answer[i - 1] * nums[i - 1]
            suffix_prod = 1  # Will be compounded by each next 'i' val
            # Now, start at 2nd to last index and work backwards
            for i in range(len(nums) - 2, -1, -1):
                suffix_prod *= nums[i + 1]
                answer[i] *= suffix_prod  # Each el in new arr is compounded by
            return answer


x = Solution
print(x.productExceptSelf(x, []))
print(x.productExceptSelf(x, [2]))
print(x.productExceptSelf(x, [1, 0]))
print(x.productExceptSelf(x, [0, 0]))
print(x.productExceptSelf(x, [-1, 2]))
print(x.productExceptSelf(x, [1, 2, 3, 4]))
print(x.productExceptSelf(x, [-1, 1, 0, -3, 3]))
