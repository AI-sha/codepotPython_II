from typing import List

class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        res = ''

        # sorting the list of strings and then checking only the first and the last words to match for letters. If letters are matching then words in between will also have matching letters as the array is sorted.

        strs = sorted(strs)  # sorted list of strings
        for i in strs[0]:  # first string of sorted list
            if strs[-1].startswith(res + i):  # last string of sorted list
                res += i  # matching letters i.e. common prefix
            else:
                break
        return res


'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

'''