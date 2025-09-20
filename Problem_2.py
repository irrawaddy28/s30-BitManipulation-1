'''
136 Single Number
https://leetcode.com/problems/single-number/description/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.

Solution:
1. XOR:
a   b   XOR
0   0   0
0   1   1
1   0   1
1   1   0

XOR has a beautiful mathematical property: a ^ a = 0 for any number a. This means when we encounter the same number twice, they neutralize each other. Additionally, 0 ^ b = b, meaning that XORing with 0 doesn't change the number.

Properties of XOR:
Commutative: a ^ b = b ^ a (order doesn't matter)
Associative: a ^ (b ^ c) = (a ^ b) ^ c (grouping doesn't matter)
Distributive: a ^ (b || c) = (a ^ b) || (a ^ c)
Inverse: a ^ a = 0 (a number is the inverse of itself)
Identity: a ^ 0 = a (XORing any value with 0 results in the original value)
Inveritibility: If c = a ^ b, then c ^ b = a. (The result of XORing two numbers can be recovered by XORing the result with one of the original numbers. This is extremely useful for encryption/decryption. This is similar to if a + b = c, then c + (-b) = a)
Non-uniqueness: If a1 ^ b1 = c, then there could be another pair (a2, b2) such that a2 ^ b2 = c

For the current problem, if nums = [4,1,2,1,2],
then 4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ 1 ^ 1 ^ 2 ^ 2 (commutative)
= 4 ^ (1 ^ 1) ^ (2 ^ 2) (associative)
= 4 ^ (0) ^ (0) (inverse)
= 4 ^ (0 ^ 0) (associative)
= 4 ^ 0 (inverse)
= 4 (identity)

https://youtu.be/vaueyO4VXgI?t=1718
Time: O(N), Space: O(1)
'''

from typing import List
def singleNumber(nums: List[int]) -> int:
    xor = 0
    for num in nums:
        xor = xor ^ num
    return xor

def run_singleNumber():
    tests = [([2,2,1], 1), ([4,1,2,1,2], 4), ([1], 1)]
    for test in tests:
        nums, ans = test[0], test[1]
        result = singleNumber(nums)
        print(f"\nnums = {nums}")
        print(f"result = {result}")
        success = (ans == result)
        print(f"Pass: {success}")
        if not success:
            print(f"Failed")
            return

run_singleNumber()