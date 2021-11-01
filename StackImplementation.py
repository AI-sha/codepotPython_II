# Python program to demonstrate Stack Implementation using list

stack = []

# append() function to push element in the stack
def push():
    element = input("Enter element:")
    stack.append(element)
    print('Initial Stack:')
    print(stack)

# pop() function to pop element from stack in LIFO order
def pop_element():
    if not stack:                     # 'not' operator to check if stack is empty. If this returns 'True' that means stack is empty
        print("Stack is empty")
    else:
        e= stack.pop()
        print('\nElement popped from the stack:',e)                     # \n will enter a line before printing this statement
        print('\nStack after element is popped:')
        print(stack)

while True:
    print("Select the operation 1. push 2. pop 3. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter correct operation")

'''
lastElement = stack[-1]  # returns last element entered in stack. i.e 'Top Element'
print('\nLast element of stack:')
print(lastElement)
'''