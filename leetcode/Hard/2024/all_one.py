# https://leetcode.com/problems/all-oone-data-structure/description/

# Design a data structure to store the strings' count with the ability to return the strings 
# with minimum and maximum counts.

# Implement the AllOne class:

# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the 
# data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 
# after the decrement, remove it from the data structure. It is guaranteed that key exists 
# in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, 
# return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, 
# return an empty string "".
# Note that each function must run in O(1) average time complexity.

# Example 1:

# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]

# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"

class AllOne:

    def __init__(self):
        self.keys = []
        self.count = []
        
    def inc(self, key: str) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            self.count[index] += 1
            while index < len(self.count) - 1:
                if self.count[index + 1] < self.count[index]:
                    self.count[index], self.count[index + 1] = self.count[index + 1], self.count[index]
                    self.keys[index], self.keys[index + 1] = self.keys[index + 1], self.keys[index]
                else:
                    break
                index += 1
        else:
            self.keys.insert(0, key)
            self.count.insert(0, 1)
        # print(f'keys = {self.keys}')
        # print(f'count: {self.count}')

    def dec(self, key: str) -> None:
        index = self.keys.index(key)
        if self.count[index] == 1:
            self.count.pop(index)
            self.keys.pop(index)
        else:
            self.count[index] -= 1
            while index > 1:
                if self.count[index - 1] > self.count[index]:
                    self.count[index], self.count[index - 1] = self.count[index - 1], self.count[index]
                    self.keys[index], self.keys[index - 1] = self.keys[index - 1], self.keys[index]
                else:
                    break
                index -= 1
        # print(f'keys = {self.keys}')
        # print(f'count: {self.count}')

    def getMaxKey(self) -> str:
        if self.keys:
            return self.keys[len(self.keys) - 1]
        return ""

    def getMinKey(self) -> str:
        if self.keys:
            return self.keys[0]
        return ""

if __name__ == '__main__':
    allOne = AllOne()
    allOne.inc('hello')
    allOne.inc('hello')
    allOne.dec('hello')
    print(allOne.getMaxKey())  # return "hello"
    print(allOne.getMinKey())  # return "hello"
    allOne.inc("leet")
    allOne.inc('hello')
    print(allOne.getMaxKey())  # return "hello"
    print(allOne.getMinKey())  # return "leet"
    allOne.inc("leet")
    allOne.inc("leet")
    print(allOne.getMaxKey())  # return "leet"
    print(allOne.getMinKey())  # return "hello"
    allOne.inc('some')
    allOne.dec('some')
