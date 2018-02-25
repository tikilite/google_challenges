"""
To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: 
the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The 
function should return an integer representing the smallest number of moves it will take for you to travel from the source 
square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by 
one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares 
will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------


Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
"""

def answer (src, dest):

    def get_coordinates(square):
        y_value = square / 8
        x_value = square % 8
        return (x_value, y_value)

    src_tuple = get_coordinates(src)
    dest_tuple = get_coordinates(dest)

    queue = [src_tuple,]
    moves = {src_tuple : 0}
    while len(queue):
        current_square = queue[0]
        queue.pop(0)
        if current_square == dest_tuple:
            return moves[current_square]

        for move in [(1,2), (2,1), (-1,-2), (-2,-1), (1,-2), (-1,2), (-2,1), (2,-1)]:
            next_square = (current_square[0] + move[0], current_square[1] + move[1])
            if next_square != dest_tuple:
                pass
            if next_square not in moves:
                moves[next_square] = moves[current_square]+1
                queue.append(next_square)
