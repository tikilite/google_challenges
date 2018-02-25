"""

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut 
in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed 
to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there 
won't ever be more pellets than you can express in that many digits.

For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
"""

def answer(n):
    n = int(n)
    i=0
    while n > 1:
        if n % 2:
            if n == 3:
                i += 2
                return i
            bin_check = "{0:b}".format(n)
            if bin_check[-2:] == "01":
                n -= 1 
            else:
                n += 1
            i += 1         
        n = n // 2
        i += 1
    return i

print answer(4), "should be 2"
print answer(15), "should be 5"
print answer(1), "should be 0"
print answer(2), "should be 1"
print answer(3), "should be 2"
print answer(17), "should be 5"



