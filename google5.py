"""
Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you 
are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, 
counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be 
solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only 
be made in cardinal directions; no diagonal moves are allowed.


Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11




"""

def answer (maze):

    src_tuple = (0, 0)
    final_row_index = len(maze) - 1
    dest_tuple = (final_row_index, len(maze[final_row_index]))

    queue = [src_tuple,]
    moves = {src_tuple : 0}
    visited = []

    while len(queue):
        current_square = queue[0]
        queue.pop(0)
        if current_square == dest_tuple:
            return moves[current_square]

        for move in [(1,0), (0,1), (-1,0), (0,-1)]:

            # print current_square
            if not 0 <= (current_square[0] + move[0]) < len(maze):
                continue
            if not 0 <= (current_square[1] + move[1]) < len(maze[0]):
                continue
            if current_square in visited:
                break
            print current_square
            visited.append(current_square)

            next_square = (current_square[0] + move[0], current_square[1] + move[1])

            if next_square not in moves:
                moves[next_square] = moves[current_square]+1
                queue.append(next_square)



maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print answer(maze)