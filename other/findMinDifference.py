# Given a list of 24-hour clock time points in "HH:MM" format, 
# return the minimum minutes difference between any two time-points in the list.
 

# Example 1:

# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:

# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
 

def findMinDifference(timePoints):
    """
    :type timePoints: List[str]
    :rtype: int
    """
    if len(set(timePoints)) < len(timePoints):
        return 0
    to_minutes = lambda x: int(x[0:2]) * 60 + int(x[3:])
    timeMins = sorted([to_minutes(x) for x in timePoints])
    diff = [timeMins[i+1] - timeMins[i] for i in range(len(timeMins)-1)]
    diff.append(1440 - timeMins[len(timeMins)-1] + timeMins[0])
    # print(timeMins)
    # print(diff)
    return min(diff)


if __name__ == '__main__':
    t = ["23:59","00:00", "11:13"]
    print(findMinDifference(t))