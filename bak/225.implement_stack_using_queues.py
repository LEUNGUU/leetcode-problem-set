# Implement Stack using Queues
#
# [Easy] [AC:44.6% 178.5K of 400.3K] [filetype:python3]
#
# Implement the following operations of a stack using queues.
#
# push(x) -- Push element x onto stack.
#
# pop() -- Removes the element on top of the stack.
#
# top() -- Get the top element.
#
# empty() -- Return whether the stack is empty.
#
# Example:
#
# MyStack stack = new MyStack();
#
# stack.push(1);
#
# stack.push(2);
#
# stack.top();   // returns 2
#
# stack.pop();   // returns 2
#
# stack.empty(); // returns false
#
# Notes:
#
# You must use only standard operations of a queue -- which means only
# push to back, peek/pop from front, size, and is empty operations are
# valid.
#
# Depending on your language, queue may not be supported natively. You
# may simulate a queue by using a list or deque (double-ended queue),
# as long as you use only standard operations of a queue.
#
# You may assume that all operations are valid (for example, no pop or
# top operations will be called on an empty stack).
#
# [End of Description]:
# Two Queues (Push O(1), Pop O(n))
from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp = deque()
        while len(self._queue) > 1:
            tmp.append(self._queue.popleft())
        res = self._queue.popleft()
        self._queue = tmp
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self._queue


# Two Queues (Push O(n), Pop O(1))
from collections import deque


class MyStack:
    def __init__(self):
        self._queue = deque()

    def push(self, x: int) -> None:
        if not self._queue:
            self._queue.append(x)
        else:
            tmp = deque()
            tmp.append(x)
            while len(self._queue) > 0:
                tmp.append(self._queue.popleft())
            self._queue = tmp

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not self._queue


# One Queue (Push O(n), Pop O(1))
from collections import deque


class MyStack:
    def __init__(self):
        self._queue = deque()

    def push(self, x: int) -> None:
        if not self._queue:
            self._queue.append(x)
        else:
            n = len(self._queue)
            self._queue.append(x)
            for _ in range(n):
                self._queue.append(self._queue.popleft())

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not self._queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
