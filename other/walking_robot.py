# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04

# A robot on an infinite XY-plane starts at point (0, 0) facing north. 
# The robot can receive a sequence of these three possible types of commands:

# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point 
# obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will 
# instead stay in its current location and move on to the next command.

# Return the maximum Euclidean distance that the robot ever gets 
# from the origin squared (i.e. if the distance is 5, return 25).

# Note:

# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.
# There can be obstacle in [0,0].
 

# Example 1:

# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 3 units to (3, 4).
# The furthest point the robot ever gets from the origin is (3, 4), 
# which squared is 32 + 42 = 25 units away.


# Example 2:

# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
# 4. Turn left.
# 5. Move north 4 units to (1, 8).
# The furthest point the robot ever gets from the origin is (1, 8), 
# which squared is 12 + 82 = 65 units away.


# Example 3:

# Input: commands = [6,-1,-1,6], obstacles = []
# Output: 36
# Explanation: The robot starts at (0, 0):
# 1. Move north 6 units to (0, 6).
# 2. Turn right.
# 3. Turn right.
# 4. Move south 6 units to (0, 0).
# The furthest point the robot ever gets from the origin 
# is (0, 6), which squared is 62 = 36 units away.
 

# Constraints:

# 1 <= commands.length <= 104
# commands[i] is either -2, -1, or an integer in the range [1, 9].
# 0 <= obstacles.length <= 104
# -3 * 104 <= xi, yi <= 3 * 104
# The answer is guaranteed to be less than 231.


def robotSim(commands, obstacles):
    """
    :type commands: List[int]
    :type obstacles: List[List[int]]
    :rtype: int
    """
    max_path = [0, 0, 0, 0] # east, north, west, south
    direction = 1  # 0 - east, 1 - north, 2 - west, 3 - south
    cur_point = [0, 0]

    for i in commands:
        if i == -1:
            direction -= 1
            if direction < 0:
                direction = 3
            continue
        if i == -2:
            direction +=1
            if direction > 3:
                direction = 0
            continue
        for j in range(i):
            match direction:
                case 0:
                    cur_point[0] += 1
                    if cur_point in obstacles:
                        cur_point[0] -= 1
                        break
                    if cur_point[0] > max_path[0]:
                        max_path[0] = cur_point[0]
                case 1:
                    cur_point[1] += 1
                    if cur_point in obstacles:
                        cur_point[1] -= 1
                        break
                    if cur_point[1] > max_path[1]:
                        max_path[1] = cur_point[1]
                case 2:
                    cur_point[0] -= 1
                    if cur_point in obstacles:
                        cur_point[0] += 1
                        break
                    if cur_point[0] < max_path[2]:
                        max_path[2] = cur_point[0]
                case 3:
                    cur_point[1] -= 1
                    if cur_point in obstacles:
                        cur_point[1] += 1
                        break
                    if cur_point[1] < max_path[3]:
                        max_path[3] = cur_point[1]
            # print('current: ', cur_point)
            
    # return pow(max_path[0], 2) + pow(max_path[1], 2) + pow(max_path[2], 2) + pow(max_path[3], 2)
    return pow(max(max_path[0], -max_path[2]), 2) + pow(max(max_path[1], -max_path[3]), 2) # + pow(max_path[2], 2) + pow(max_path[3], 2)


if __name__ == '__main__':
    print(robotSim([4,-1,3], []))
    print(robotSim([4,-1,4,-2,4], [[2, 4]]))
    print(robotSim([6,-1,-1,6], []))
    print(robotSim([-2,-1,8,9,6], [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]))
    # print(robotSim([2,-1,8,-1,6], [[1,5],[-5,-5],[0,4],[-1,-1],[4,5],[-5,-3],[-2,1],[-2,-5],[0,5],[0,-1]]))
