from c_Queues_Stack.stacks import Stack

"""
The usual convention followed in mathematics is the infix expression. Operators like + and * appear 
between the two numbers involved in the calculation:

`6 + 3 * 8 - 4`

Another convention is the postfix expression where the operators appear after the two numbers 
involved in the expression. In postfix, the expression written above will be presented as:

`6 3 8 * + 4 -`

The two digits preceding an operator will be used with that operator

From the first block of digits 6 3 8, we pick the last two which are 3 and 8.
Reading the operators from left to right, the first one is *. The expression now becomes 3 * 8
The next number is 6 while the next operator is +, so we have 6 + 8 * 3.
The value of this expression is followed by 4, which is right before -. Hence we have 6 + 8 * 3 - 4.
Implement a function called evaluatePostFix() that will compute a postfix expression given to it as a string.
"""


def evaluate_post_fix(exp):
    stack = Stack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
            else:
                # use top two numbers and evaluate
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        # final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"


if __name__ == "__main__":
    print("Result of expression (921*-8-4+) : " + str(evaluate_post_fix("921*-8-4+")))
    print("Result of expression (921*-8--4+) : " + str(evaluate_post_fix("921*-8--4+")))
