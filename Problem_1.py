'''
29 Divide Two Integers
https://leetcode.com/problems/divide-two-integers/description/

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.


Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0

Solution:
1. Find increasingly larger multiples of the divisor (divisor * 2^n, created by left shifting the divisor by n bits) that is still smaller than the dividend, subtract it from the dividend (dividend - divisor * 2^n) to get a new reduced divident, and repeat. We are taking the biggest possible bite out of the dividend each time instead of nibbling (subtracting divisor multiple times).
Each bite is expressed as divisor*(2^0 + 2^1 + ... 2^k) where k is such that bite < dividend.

More explanation:
Let dividend = 1000, divisor = 5
quotient = 1000/5 = 200
                  =    (2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6)
                     + (2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5)
                     + (2^0 + 2^1 + 2^2)
                     + (2^0 + 2^1)
                  = 127 + 63 + 7 + 3
                  = 190 + 7 + 3
                  = 200

Thus,
1000 = 5*200
     =   5*(2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6)
       + 5*(2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5)
       + 5*(2^0 + 2^1 + 2^2)
       + 5*(2^0 + 2^1)
     = 5*127 + 5*63  5*7 + 5*3
     = 635 + 315 + 35 + 15
     = 1000

Hence, at step 1, the biggest no./bite we can remove from 1000 is 635. Because if we try to remove a bigger number, this would result in removing 635 + 5*2^7 = 635 + 640 = 1275 which is > dividend (1000).

After removing 635 from 1000, we are left with 365. At step 2, the biggest no. we can remove from 365 is 315.

After removing 315 from 365, we are left with 50. At step 3, the biggest no. we can remove from 40 is 35.

After removing 35 from 50, we are left with 15. At step 4, the biggest no. we can remove from 15 is 15.

After removing 15 from 15, we are left with 0 which is smaller than the divisor 5. We cannot remove anything more. We return the quotient.

Dry run:
num = 1000, den = 5, n = 0, q = 1, den*q = 5, num - den*q = 995, quotient = 1
num = 995, den = 5, n = 1, q = 2, den*q = 10, num - den*q = 985, quotient = 3
num = 985, den = 5, n = 2, q = 4, den*q = 20, num - den*q = 965, quotient = 7
num = 965, den = 5, n = 3, q = 8, den*q = 40, num - den*q = 925, quotient = 15
num = 925, den = 5, n = 4, q = 16, den*q = 80, num - den*q = 845, quotient = 31
num = 845, den = 5, n = 5, q = 32, den*q = 160, num - den*q = 685, quotient = 63
num = 685, den = 5, n = 6, q = 64, den*q = 320, num-den*q = 365, quotient = 127

since next n = 7, num -  den << n = 365 - 5*128 = 365 - 640 < 0, we start a new loop
resetting q = 2^0 = 1

num = 365, den = 5, n = 0, q = 1, den*q = 5, num - den*q = 360, quotient = 128
num = 360, den = 5, n = 1, q = 2, den*q = 10, num - den*q = 350, quotient = 130
num = 350, den = 5, n = 2, q = 4, den*q = 20, num - den*q = 330, quotient = 134
num = 330, den = 5, n = 3, q = 8, den*q = 40, num - den*q = 290, quotient = 142
num = 290, den = 5, n = 4, q = 16, den*q = 80, num - den*q = 210, quotient = 158
num = 210, den = 5, n = 5, q = 32, den*q = 160, num - den*q = 50, quotient = 190

since next n = 6, num -  den << n = 50 - 5*64 = 50 - 320 < 0, we start a new loop
resetting q = 2^0 = 1

num = 50, den = 5, n = 0, q = 1, den*q = 5, num - den*q = 45, quotient = 191
num = 45, den = 5, n = 1, q = 2, den*q = 10, num - den*q = 35, quotient = 193
num = 35, den = 5, n = 2, q = 4, den*q = 20, num - den*q = 15, quotient = 197

since next n = 3, num -  den << n = 15 - 5*8 = 15 - 40 < 0, we start a new loop
resetting q = 2^0 = 1

num = 15, den = 5, n = 0, q = 1, den*q = 5, num - den*q = 10, quotient = 198
num = 10, den = 5, n = 1, q = 2, den*q = 10, num - den*q = 0, quotient = 200

since num <= den, we cannot divide this any further. We return the quotient = 200

https://youtu.be/pBD4B1tzgVc?t=244 (dry run 22/3, quotient expressed as sum of powers of 2, easy to understand)
https://youtu.be/vaueyO4VXgI?t=4046
Time: O((log N)^2), Space: O(1)

'''
def divide(dividend, divisor):
    ''' Time: O((log N)^2), Space: O(1) '''
    LIMITS = [-2**31, 2**31 - 1]
    if divisor == 1:
        return dividend
    elif dividend == divisor:
        return 1
    elif dividend == 0 or divisor == 0:
        return 0

    sign = 1
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        sign = -1

    num = abs(dividend)
    den = abs(divisor)

    quotient = 0 # running sum of quotients
    while num >= den:
        n = 0 # no. of bits to shift
        while num - (den << n) >= 0: # den << n = den*(2^n)
            q = 1 << n # 2^n
            quotient += q
            #print(f"num = {num}, den = {den}, n = {n}, q = {q}, den*q = {den*q}, num - den*q = {num - (den << n)}, quotient = {quotient}")
            num = num - (den << n)
            n += 1

    # Bound quotient to the range [LIMITS[0], LIMITS[1]]
    quotient = max(LIMITS[0], quotient)
    quotient = min(LIMITS[1], quotient)
    quotient = sign*quotient
    return quotient

def run_divide():
    tests = [(1000, 5, 200),
             (28, 3, 9),
             (28, -3, -9),
             (-28, 3, -9),
             (-28, -3, 9),
             (7, -3, -2),
    ]
    for test in tests:
        dividend, divisor, ans = test[0], test[1], test[2]
        print(f"\ndividend = {dividend}")
        print(f"divisor = {divisor}")
        quotient = divide(dividend, divisor)
        print(f"quotient = {quotient}")
        success = (ans == quotient)
        print(f"Pass: {success}")
        if not success:
            print(f"Failed")
            return

run_divide()