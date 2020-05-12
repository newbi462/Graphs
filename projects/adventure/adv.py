from room import Room
from player import Player
from world import World

from util import Stack, Queue  # These may come in handy

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
####world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
my_key_graph = {
    "all_rooms": []
}
traversal_path = []

print(player.current_room.id)#room I am in
print(player.current_room.x)# X room grit point
print(player.current_room.y)# X room grit point
#print(player.current_room.get_exits())


### Get all the rooms
#can I get the rooms use DFT?
s = Stack()
s.push(player.current_room) #difrent paramiter
all_rooms = set() # Keep track of visited nodes

while s.size() > 0:# Repeat until queue is empty
    here = s.pop() # Dequeue first vert
    if here.id not in all_rooms: # If it's not visited:
        #print(v)
        all_rooms.add(here.id) # Mark visited
        my_key_graph[ str(here.id) ] = {
            "visited": False,
            "n": None,
            "s": None,
            "e": None,
            "w": None
        }
        my_key_graph["all_rooms"].append(here.id)
        for x in here.get_exits():
            s.push(here.get_room_in_direction(x))
#for room in all_rooms:
#    print(room)
print(my_key_graph)

### Path fo go from room[0] to next taget not visted to do that...
### from new room[curent] path to next unvisited
## repeat untill all 500 visited


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
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
