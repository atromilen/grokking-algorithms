
def squarePlotsDivision(biggest, lowest):
    print('Plot of {} x {}'.format(biggest, lowest))
    if (biggest % lowest) == 0:
        return lowest
    else:
        return squarePlotsDivision(lowest, biggest % lowest)

# In this example, we want to divide a plot of 1680 x 640 metters into squares as big as possible.
# Using Divide & Conquer, we figure out what are the biggest and smallest boxes we can use to divide:
# We need to know that is the smaller box to complete the full 1680 meassurement. 
# i.e. 1680 = 640 + 640 + 400 (this last is smallest box than we can use) 
# This 400 are finded using remainder operation: 1680 % 640 = 400 (remainder)
# Our algorithm ends up with the smallest box possible when the remainder between biggest and 
# smallest will be zero.
# 
# This solution is bassed on Euclide´s algorithm:
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm 

biggest = 50
lowest = 50
square = squarePlotsDivision(biggest, lowest)
print('Smaller square for a plot of {}x{}: {}'.format(biggest, lowest, square))