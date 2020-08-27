# Implement Queue using Stacks
#
# [Easy] [AC:49.0% 213.9K of 436.6K] [filetype:python3]
#
# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
#
# pop() -- Removes the element from in front of queue.
#
# peek() -- Get the front element.
#
# empty() -- Return whether the queue is empty.
#
# Example:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
#
# queue.push(2);
#
# queue.peek();  // returns 1
#
# queue.pop();   // returns 1
#
# queue.empty(); // returns false
#
# Notes:
#
# You must use only standard operations of a stack -- which means only
# push to top, peek/pop from top, size, and is empty operations are
# valid.
#
# Depending on your language, stack may not be supported natively. You
# may simulate a stack by using a list or deque (double-ended queue),
# as long as you use only standard operations of a stack.
#
# You may assume that all operations are valid (for example, no pop or
# peek operations will be called on an empty queue).
#
# [End of Description]:
# Two Stacks (Push O(n), Pop O(1))
class MyQueue:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def push(self, x: int) -> None:
        if not self._stack1:
            self._stack1.append(x)
        else:
            while len(self._stack1) > 0:
                self._stack2.append(self._stack1.pop())
            self._stack1.append(x)
            while len(self._stack2) > 0:
                self._stack1.append(self._stack2.pop())

    def pop(self) -> int:
        return self._stack1.pop()

    def peek(self) -> int:
        return self._stack1[-1]

    def empty(self) -> bool:
        return not self._stack1

# Two Stacks(Push O(1), Pop O(n))
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack1 = []
        self._stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for _ in range(len(self._stack1)):
            self._stack2.append(self._stack1.pop())
        removed = self._stack2.pop()
        for _ in range(len(self._stack2)):
            self._stack1.append(self._stack2.pop())
        return removed

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._stack1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
