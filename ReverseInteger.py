class ReverseInteger:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:  # outside signed bit integer range
            return 0
        else:
            strg = str(x)
            if x >= 0:  # say strg = 123
                revst = strg[::-1]  # revst will be equal to 321
            else:  # say strg = -123
                temp = strg[1:]  # leaving the first character of string ie '-', temp = 123
                temp2 = temp[::-1]  # temp2 = 321 (reverse of temp)
                revst = "-" + temp2  # revst = -321
            if int(revst) >= 2 ** 31 - 1 or int(revst) <= -2 ** 31:  # outside signed bit integer range
                return 0
            else:
                return int(revst)


'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321

'''