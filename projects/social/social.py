import random


class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self, start=None):
        self.length = 1 if start is not None else 0
        self.head = SLLNode(start) if start else None
        self.tail = SLLNode(start) if start else None

    def enqueue(self, value):
        if self.length == 0:
            self.head = self.tail = SLLNode(value)
            self.length += 1
        else:
            self.tail.next = SLLNode(value)
            self.tail = self.tail.next
            self.length += 1

    def dequeue(self):
        if len(self) > 0:
            return_node = self.head
            self.head = self.head.next
            self.length -= 1
            return return_node.value
        else:
            return None

    def __len__(self):
        return self.length


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

        # Add users
        for user_id in range(num_users):
            self.add_user("User id: " + str(user_id+1))

        # Create friendships

        possible_friends = []

        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friends.append((user_id, friend_id))

        random.shuffle(possible_friends)

        for i in range(num_users * avg_friendships // 2):
            ship = possible_friends[i]
            self.add_friendship(ship[0], ship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {user_id: []}  # Note that this is a dictionary, not a set
        q = Queue([user_id])
        while len(q) > 0:
            path = q.dequeue()
            for friend in self.friendships[path[-1]]:
                if friend not in visited:
                    visited[friend] = [*path, friend]
                    q.enqueue(visited[friend])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    # To calculate percentage of friends in social network
    # compared to all users
    extended_network_list = []
    for network in connections.values():
        extended_network_list += network
    extended_network_set = set(extended_network_list)
    percentage = len(extended_network_set) / len(sg.users) * 100
    print(f"\npercentage of users in extended network: {percentage}%")
