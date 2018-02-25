"""
Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, 
and how many bunnies can fit through at a time in each direction of every corridor in between, 
figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function answer(entrances, exits, path) that takes an array of integers denoting where 
the groups of gathered bunnies are, an array of integers denoting where the escape pods are 
located, and an array of an array of integers of the corridors, returning the total number of 
bunnies that can get through at each time step as an int. The entrances and exits are disjoint 
and thus will never overlap. The path element path[A][B] = C describes that the corridor going 
from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the 
corridors and at most 2000000 bunnies that will fit at a time.

Test cases
==========

Inputs:
    (int list) entrances = [0]
    (int list) exits = [3]
    (int) path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

answer = 16

"""
def answer(entrances, exits, path):
    path_dict = {}
    for entrance in entrances:
        count = 0
        for passage in path[entrance]:
            if count not in exits:
                if passage:
                    if count in path_dict:
                        path_dict[count] += passage
                    else:
                        path_dict[count] = passage
            if count not in exits and count not in entrances:
                entrances.append(count)
            count += 1
    
    second_dict = {}
    dict_keys = path_dict.keys()
    for corridor in dict_keys:
        count = 0
        for passage in path[corridor]:
            if passage:
                if passage < path_dict[corridor]:
                    if count in second_dict:
                        second_dict[count] += passage
                    else:
                        second_dict[count] = passage
                    path_dict[corridor] = path_dict[corridor] - passage
                else: 
                    if count in second_dict:
                        second_dict[count] += path_dict[corridor]
                    else:
                        second_dict[count] = path_dict[corridor]
            count += 1

    bunny_count = 0
    for each in exits:
        if each in second_dict:
            bunny_count += second_dict[each]
    if bunny_count > 2000000:
        bunny_count = 2000000
    return bunny_count
    


entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

# path = [
#   [0, 0, 1, 0, 0, 0],  # Room 0: Bunnies
#   [0, 0, 0, 0, 0, 0],  # Room 1: Bunnies
#   [0, 0, 0, 0, 1, 6],  # Room 2: Intermediate room
#   [0, 0, 0, 0, 0, 0],  # Room 3: Intermediate room
#   [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
#   [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
# ]

# entrances = [0]
# exits = [3]
# path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

# path = [
#   [0, 0, 4, 6, 0, 0, 0],  # Room 0: Bunnies
#   [0, 0, 5, 2, 0, 0, 0],  # Room 1: Bunnies
#   [0, 0, 0, 0, 4, 4, 0],  # Room 2: Intermediate room
#   [0, 0, 0, 0, 6, 6, 0],  # Room 3: Intermediate room
#   [0, 0, 0, 0, 0, 0, 2],  # Room 4: Escape pods
#   [0, 0, 0, 0, 0, 0, 2],
#   [0, 0, 0, 0, 0, 0, 0]  # Room 5: Escape pods
# ]




# entrances = [0, 1, 2]
# exits = [6]

print answer(entrances, exits, path)







