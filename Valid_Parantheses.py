class Valid_Parantheses:
    def isValid(self, s: str) -> bool:  # type of s is string and return type of function is boolean

        stack = []  # to keep track of opening brackets

        mapping = {")": "(", "}": "{", "]": "["}  # comma separated key:value pairs in a map/dictionary

        # for every character in the expression provided
        for char in s:

            # if the character is a closing bracket by looking if the character is a key of the map
            if char in mapping:

                # top_element = stack.pop() if stack else '#'

                # pop the topmost element from the stack if it is not empty
                # , otherwise assign a dummy '#' to top_element variable
                if not stack:  # 'not' operator: to determine if list is empty. empty list evaluates to false, so stack = false (if list empty) then not stack = true, so if is exceuted
                    top_element = '#'
                else:
                    top_element = stack.pop()

                if mapping[char] != top_element:
                    return False

            else:
                # We have an opening bracket, push it onto the stack
                stack.append(char)

        # In the end, if stack is empty, we have a valid expression
        # for cases like {{{}, the stack won't be empty
        return not stack


    ''' 
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Input: s = "()"
Output: true

Input: s = "([)]"
Output: false

'''