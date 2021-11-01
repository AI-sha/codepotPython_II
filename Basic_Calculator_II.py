class BasicCalulatorII:
    def calculate(self, s: str) -> int:

        stack = []
        curr = 0
        ope = "+"

        # If the string is empty, return output as 0
        if not s:
            return 0

        # Create a set with all the operators
        operators = {'+', '-', '*', '/'}

        # create a set using a set
        nums = set(str(x) for x in range(0, 10))  # inside the set function is a list comprehension

        # loop for all elements of the string expression , say = "3+2*2"
        for i in range(0, len(s)):
            char = s[i]

            # if the character is a digit
            if char in nums:
                curr = curr * 10 + int(char)  # int(char) used to return the string as a integer

            if char in operators or i == len(s) - 1:  # to check the second condition?

                if ope == '+':
                    stack.append(curr)

                elif ope == '-':
                    stack.append(-curr)

                elif ope == '*':
                    stack[-1] *= curr  # take the last item and multiply it with current and store at the last

                elif ope == '/':
                    stack[-1] = int(stack[-1] / curr)

                curr = 0
                ope = char

        return sum(stack)

        '''
        Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Input: s = "3+2*2"
Output: 7
'''
