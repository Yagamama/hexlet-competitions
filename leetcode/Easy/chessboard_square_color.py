# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/

# You are given two strings, coordinate1 and coordinate2, representing the 
# coordinates of a square on an 8 x 8 chessboard.

# Below is the chessboard for reference (a1 is black)

# Return true if these two squares have the same color and false otherwise.

# The coordinate will always represent a valid chessboard square. 
# The coordinate will always have the letter first (indicating its column), 
# and the number second (indicating its row).

# Example 1:
# Input: coordinate1 = "a1", coordinate2 = "c3"
# Output: true
# Explanation:
# Both squares are black.

# Example 2:
# Input: coordinate1 = "a1", coordinate2 = "h3"
# Output: false
# Explanation:
# Square "a1" is black and "h3" is white.

def checkTwoChessboards(coordinate1, coordinate2):
    nums = {'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            }
    first = nums[coordinate1[0]] + int(coordinate1[1])
    second = nums[coordinate2[0]] + int(coordinate2[1])
    return first % 2 == second % 2


if __name__ == '__main__':
    print(checkTwoChessboards("a1", "c3"))  # True
    print(checkTwoChessboards("a1", "h3"))  # False
