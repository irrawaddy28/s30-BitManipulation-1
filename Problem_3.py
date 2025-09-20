'''
260 Single Number III
https://leetcode.com/problems/single-number-iii/description/

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
2 <= nums.length <= 3 * 104
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.

Solution:
1. Hash map
We count each number using a HashMap to track frequency. Then we loop through the map to find numbers that appear only once. We return the two such numbers we find in an array.
Time: O(N), Space: O(N)

2. XOR
Step 1: First, we XOR all numbers in the nums array. This cancels out duplicate numbers resulting in a value comprising of the XORs of the two unique numbers. Let's call this xor1

Step 2: Compute magic
magic = xor1 and (-xor1) (bitwise and of number and its 2's complement)

Property of magic number:
If num1 and num2 are numbers that occur only once in nums array, then
magic && num1 = 0
magic && num2 != 0
Hence, one of the numbers which when bitwise and-ed with magic will result in a non-zero value. We can use this as a filter to pick up one of the unique nos.

Step 3: XOR only those nos. in the nums array for which magic & num != 0. Call this filtered XOR as xor2. At this point, xor2 should contain one of the unique nos. XORing xor2 with xor1 retrieves the other unique number
https://youtu.be/vaueyO4VXgI?t=2380 - https://youtu.be/vaueyO4VXgI?t=3181 (dry run)
Time: O(N), Space: O(1)

'''
from typing import List
def singleNumber_Hash(nums: List[int]) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        result = []
        for key in map:
            if map[key] == 1:
                result.append(key)

        return result
def singleNumber_XOR(nums: List[int]) -> List[int]:

    xor1 = 0
    for num in nums:
        xor1 = xor1 ^ num

    # Compute magic
    magic = xor1 and (-xor1)

    # Property of magic number:
    # If num1 and num2 are numbers that occur only once in nums array, then
    # magic && num1 = 0
    # magic && num2 != 0
    # Hence, one of the numbers will result in non-zero.

    # XOR all those nos. in the nums array for which magic & num != 0
    xor2 = 0
    for num in nums:
         # using magic, filter in elements which occur only once
         # some numbers which occur twice could be filtered in
        if magic & num != 0:
            xor2 = xor2 ^ num

    # At this point, xor2 should contain a number which occured only once
    # XORing xor2 with xor1 retrieves the other unique number
    result = [xor2, xor2 ^ xor1]
    return result

def run_singleNumber():
    tests  = [([1,2,1,3,2,5], [3,5]), ([-1,0], [-1,0]),
              ([0,1], [0,1]), ([9,2,7,5,9,7], [2,5]),
              ([-1139700704,-1653765433], [-1139700704,-1653765433]),
    ]
    tests = [([-1139700704,-1653765433], [-1139700704,-1653765433])]
    for test in tests:
        nums, ans = test[0], test[1]
        print(f"\nnums = {nums}")
        for method in ['hash', 'xor']:
            if method == 'hash':
                result = singleNumber_Hash(nums)
            elif method == 'xor':
                result = singleNumber_XOR(nums)
            print(f"Method {method}: result = {result}")
            success = (sorted(ans) == sorted(result))
            print(f"Pass: {success}")
            if not success:
                print(f"Failed")
                return

run_singleNumber()