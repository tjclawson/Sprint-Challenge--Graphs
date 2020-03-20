from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = set()
room_list = []


def dft_recursive(room_id):

    room_list.append(room_id)
    if room_id not in visited:
        visited.add(room_id)
        for key, id in room_graph[room_id][1].items():
            if id not in visited:
                dft_recursive(id)
                room_list.append(room_id)


def convert_list_of_rooms_to_directions(rooms):
    for i in range(0, len(rooms) - 1):
        for direction, id in room_graph[rooms[i]][1].items():
            if id == rooms[i + 1]:
                traversal_path.append(direction)


dft_recursive(player.current_room.id)
convert_list_of_rooms_to_directions(room_list)
print(room_list)

testing = []
for i in range(0, len(traversal_path)):
    testing.append((room_list[i], traversal_path[i]))

print(testing)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
