"""


# Solution using Recursion (without Memoization):  time complexity O(2^n)
#Consider this: If we wanted to find how many ways there are to climb to the 250th step, the number of #operations we would have to do is approximately equal to the number of atoms in the universe.

#Notice the 3 components of the DP framework used below:

class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            #A function that returns the answer to the problem for a given state. Component 1
            #Base cases: when i is less than 3 there are i ways to reach the ith stair. component 3
            if i <= 2:
                return i

            # If i is not a base case, then use the recurrence relation. Component 2
            return dp(i - 1) + dp(i - 2)

        return dp(n)

"""

# Solution using Top down DP (i.e with Memoization):  time complexity O(n)
"""astronomically better, literally"""


class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i <= 2:
                return i
            if i not in memo:
                # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
                # store the result inside a hashmap to refer to in the future.
                memo[i] = dp(i - 1) + dp(i - 2)

            return memo[i]

        memo = {}  # hashmap to assist in caching i.e. memoization
        return dp(n)


"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
