from c_Queues_Stack.stacks import Stack

"""
In this problem, you have to implement the `is_balanced()` function which will take a string containing only curly {},
square [], and round () parentheses.
The function will tell us whether all the parentheses in the string are balanced or not.
For all the parentheses to be balanced, every opening parenthesis must have a closing one. 
The order in which they appear also matters. For example, {[]} is balanced, but {[}] is not.
"""


def is_balanced(exp):
    open_parentheses = {'{', '(', '['}
    parentheses_mapping = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    stack = Stack()

    for char in exp:
        if char in open_parentheses:
            stack.push(char)
        else:
            opened = stack.pop()
            mapping_closed = parentheses_mapping[opened]
            print('opened', opened, 'mapping_closed', mapping_closed)
            if mapping_closed != char:
                return False

    return True


if __name__ == "__main__":
    # Example 1
    input_string = "{[()]}"  # balanced string
    result = str(is_balanced(input_string))
    print("Input string \"" + input_string + "\" is balanced: " + result)
    # Example 2
    input_string = "{[([({))]}}"  # imbalanced string
    result = str(is_balanced(input_string))
    print("Input string \"" + input_string + "\" is balanced: " + result)
    # Example 3
    input_string = ""  # an empty string is balanced
    result = str(is_balanced(input_string))
    print("Input string \"" + input_string + "\" is balanced: " + result)
