import random
from util import Stack, Queue  # These may come in handy

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")#methosd name difrenbtr

        # Create friendships
        possible_friendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        #print(self.users)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
                # use BFT to get to each person in the connected component
        # use BFS to get to the shortest path to each component

        def bfs(starting_vertex, destination_vertex):
            queue = Queue()
            queue.enqueue([starting_vertex])
            # Create a Set to store visited vertices
            visited = set()
            # While the queue is not empty...
            while queue.size() > 0:
                # Dequeue the first PATH
                path = queue.dequeue()
                # Grab the last vertex from the PATH
                vertex = path[-1]
                # If that vertex has not been visited...
                if vertex not in visited:
                    # CHECK IF IT'S THE TARGET
                    visited.add(vertex) # Mark it as visited...
                    if vertex == destination_vertex:
                        return path # IF SO, RETURN PATH
                    else:# Then add A PATH TO its neighbors to the back of the queue
                        for x in self.friendships[vertex]:
                            # _COPY_ THE PATH
                            # APPEND THE NEIGHOR TO THE BACK
                            queue.enqueue([*path, x])
            return [starting_vertex, destination_vertex]

        #USE bft
        q = Queue()
        q.enqueue(self.friendships[user_id]) #difrent paramiter
        visited = {}

        while q.size() > 0:# Repeat until queue is empty
            v = q.dequeue() # Dequeue first vert
            for next_vert in v: # retruned values from above
                if next_vert not in visited and next_vert != user_id:
                    visited[next_vert] = bfs(user_id, next_vert)
                    q.enqueue(self.friendships[next_vert])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
