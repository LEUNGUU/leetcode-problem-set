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
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x: int) -> None:
        # stack is empty
        if not self._stack:
            node = (x, x)
        else:
            # not empty
            if self._stack[-1][1] < x:
                node = (x, self._stack[-1][1])
            else:
                node = (x, x)
        self._stack.append(node)

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
