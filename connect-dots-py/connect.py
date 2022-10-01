# Python3 program to get minimum lines to cover
# all the points

# Utility method to get gcd of a and b
def gcd(a, b):
	if (b == 0):
		return a
	return gcd(b, a % b)

# method returns reduced form of dy/dx as a pair
def getReducedForm(dy, dx):
	g = gcd(abs(dy), abs(dx))

	# get sign of result
	sign = (dy < 0) ^ (dx < 0)

	if (sign):
		return (-abs(dy) // g, abs(dx) // g)
	else:
		return (abs(dy) // g, abs(dx) // g)

# /* method returns minimum number of lines to
#	 cover all points where all lines goes
#	 through (xO, yO) */
def minLinesToCoverPoints(points, N, xO, yO):
	
	# set to store slope as a pair
	st = dict()
	minLines = 0

	# loop over all points once
	for i in range(N):
		
		# get x and y co-ordinate of current point
		curX = points[i][0]
		curY = points[i][1]

		temp = getReducedForm(curY - yO, curX - xO)

		# if this slope is not there in set,
		# increase ans by 1 and insert in set
		if (temp not in st):
			st[temp] = 1
			minLines += 1

	return minLines

# Driver code
xO = 1
yO = 0

points =[[-1, 3],
		[4, 3],
		[2, 1],
		[-1, -2],
		[3, -3]]
points_2 = [
    [4,3],
    [3,-3],
    [-1,3],
    [-1,-2]
]
# grid_points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [11, 0], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [12, 0], [12, 1], [12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7]]
grid_points = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], 
[12, 9], [13, 2], [13, 3], [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [14, 9]]

N = len(grid_points)
print(minLinesToCoverPoints(grid_points, N, xO, yO))

N2 = len(points)
print(minLinesToCoverPoints(points, N2, xO, yO))

# This code is contributed by mohit kumar 29
