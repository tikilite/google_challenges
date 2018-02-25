"""
Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different 
types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different 
types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be 
lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of 
bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the 
second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) 
or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be 
built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because 
Commander Lambdas not made of money!

Inputs:
    (int) n = 3
Output:
    (int) 1
"""
def answer (n):
    table = [[0 for i in range(n + 1)] for j in range(n + 1)]
    table[0][0] = 1

    for step in range(1, n + 1):
        for leftover in range(0, n + 1):
            table[step][leftover] = table[step - 1][leftover]
            if leftover >= step:
                table[step][leftover] += table[step - 1][leftover - step]

    return (table[n][n] - 1)

print answer(6)