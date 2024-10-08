# https://leetcode.com/problems/design-circular-deque/description/

# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, 
# or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, 
# or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, 
# or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, 
# or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
 

# Example 1:

# Input
# ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", 
#  "deleteLast", "insertFront", "getFront"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 2, true, true, true, 4]

# Explanation
# MyCircularDeque myCircularDeque = new MyCircularDeque(3);
# myCircularDeque.insertLast(1);  // return True
# myCircularDeque.insertLast(2);  // return True
# myCircularDeque.insertFront(3); // return True
# myCircularDeque.insertFront(4); // return False, the queue is full.
# myCircularDeque.getRear();      // return 2
# myCircularDeque.isFull();       // return True
# myCircularDeque.deleteLast();   // return True
# myCircularDeque.insertFront(4); // return True
# myCircularDeque.getFront();     // return 4

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.maxlen = k
        
    def insertFront(self, value: int) -> bool:
        if len(self.deque) == self.maxlen:
            return False
        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.deque) == self.maxlen:
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if not self.deque:
            return False
        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if not self.deque:
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if not self.deque:
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if not self.deque:
            return -1
        return self.deque[len(self.deque) - 1]

    def isEmpty(self) -> bool:
        return not self.deque

    def isFull(self) -> bool:
        return len(self.deque) == self.maxlen


if __name__ == '__main__':
    myCircularDeque = MyCircularDeque(3)
    print(myCircularDeque.insertLast(1))  # return True
    print(myCircularDeque.insertLast(2))  # return True
    print(myCircularDeque.insertFront(3)) # return True
    print(myCircularDeque.insertFront(4)) # return False, the queue is full.
    print(myCircularDeque.getRear())      # return 2
    print(myCircularDeque.isFull())       # return True
    print(myCircularDeque.deleteLast())   # return True
    print(myCircularDeque.insertFront(4)) # return True
    print(myCircularDeque.getFront())     # return 4
