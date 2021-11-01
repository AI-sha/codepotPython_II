class LongestSubtstringWithoutRepeatingChar:
    '''
    Brute force : time limit exceeded
    '''

    def lengthOfLongestSubstring(self, s: str) -> int:

        def check(start, end):  # function that returns true if all char of subsstring are unique

            chars = [0] * 128  # set of 128
            for i in range(start, end + 1):  # adding 1 to end as range function excludes end limit

                c = s[i]  # first character of string
                chars[ord(c)] += 1  # ord() returns the integer value which represents the char. A = 65
                # at that integer position we add 1
                if chars[ord(c)] > 1:  # check if the integer position has more than 1 count
                    return False  # if count at particular integer position is > 1, it means duplicate
            return True

        n = len(s)

        res = 0
        for i in range(n):  # 2 nested loops used to fetch all the substrings
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)  # length of longest unique substring
        return res


'''
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''