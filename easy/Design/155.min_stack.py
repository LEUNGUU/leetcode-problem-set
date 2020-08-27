# Min Stack
#
# [Easy] [AC:44.0% 549.6K of 1.2M] [filetype:python3]
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
# push(x) -- Push element x onto stack.
#
# pop() -- Removes the element on top of the stack.
#
# top() -- Get the top element.
#
# getMin() -- Retrieve the minimum element in the stack.
#
# Example 1:
#
# Input
#
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
#
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
#
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
#
# MinStack minStack = new MinStack();
#
# minStack.push(-2);
#
# minStack.push(0);
#
# minStack.push(-3);
#
# minStack.getMin(); // return -3
#
# minStack.pop();
#
# minStack.top();    // return 0
#
# minStack.getMin(); // return -2
#
# Constraints:
#
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
#
# [End of Description]:
# Stack of Value/Minimum pairs
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x: int) -> None:
        # If the stack is empty, then the min value
        # must be the first value we add
        if not self._stack:
            self._stack.append((x, x))
        else:
            # If the stack is not empty
            cur_min = self._stack[-1][1]
            self._stack.append((x, min(x, cur_min)))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# Two Stack (Use a new stack to store the minimum values)
class MinStack:
    def __init__(self):
        """
        initialize your data structure here
        """
        self._stack = []
        self._min_stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self) -> None:
        if self._min_stack[-1] == self._stack[-1]:
            self._min_stack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


# Improve Two Stack (avoid push lots of same value into a stack)
class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, x: int) -> None:
        # we always put the number onto the main stack
        self._stack.append(x)

        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self._min_stack or x < self._min_stack[-1][0]:
            self._min_stack.append([x, 1])
            return

        # If this number is equal to what is currently at the
        # top of the min stack, then increment the count at the
        # top by 1
        if x == self._min_stack[-1][0]:
            self._min_stack[-1][1] += 1

    def pop(self) -> None:
        # If the top of min stack is the same as the top of stack
        # then we need to decrement the coutn at the top by 1.
        if self._min_stack[-1][0] == self._stack[-1]:
            self._min_stack[-1][1] -= 1

        # If the count at the top of min stack is now 0,
        # then remove that value as we're done with it.
        if self._min_stack[-1][1] == 0:
            self._min_stack.pop()

        # And like before, pop the top of the main stack
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
