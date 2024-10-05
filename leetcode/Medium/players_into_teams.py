# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

# You are given a positive integer array skill of even length n where skill[i] 
# denotes the skill of the ith player. Divide the players into n / 2 teams of 
# size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the players 
# on that team.

# Return the sum of the chemistry of all the teams, or return -1 if there is no way 
# to divide the players into teams such that the total skill of each team is equal.

# Example 1:

# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation: 
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each 
# team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

# Example 2:

# Input: skill = [3,4]
# Output: 12
# Explanation: 
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.

# Example 3:

# Input: skill = [1,1,2,3]
# Output: -1
# Explanation: 
# There is no way to divide the players into teams such that the total skill of each team is equal.


def dividePlayers(skill):
    chemistry = 0
    teams = []
    skill = sorted(skill)
    sums = set()
    len_skill = len(skill)
    for i in range(len_skill // 2):
        teams.append((skill[i], skill[len_skill - i - 1]))
        sums.add(skill[i] + skill[len_skill - i - 1])
        if len(sums) > 1:
            return -1
        chemistry += skill[i] * skill[len_skill - i - 1]
    return chemistry


if __name__ == '__main__':
    print(dividePlayers([3,2,5,1,3,4]))  # 22
    print(dividePlayers([3,4]))  # 12
    print(dividePlayers([1,1,2,3]))  # -1
