# Initialize the users
users = [
    { "id": 0, "name": "Hero"},
    { "id": 1, "name": "Dunn"},
    { "id": 2, "name": "Sue"},
    { "id": 3, "name": "Chi"},
    { "id": 4, "name": "Thor"},
    { "id": 5, "name": "Clive"},
    { "id": 6, "name": "Hicks"},
    { "id": 7, "name": "Devin"},
    { "id": 8, "name": "Kate"},
    { "id": 9, "name": "Klein"},
]

# Initialize the friendship betwee the Users
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize user list with empty friendships
friendships = {user["id"]: [] for user in users}

# Fill friendships with friends
for i, j in friendship_pairs:
    if i in friendships and j in friendships:
        friendships[i].append(j)
        friendships[j].append(i)
    else:
        print(f"Warning: User with ID {i} or {j} does not exists.")

# Print out the result
print(f"Benutzer: {users}")
print(f"Beziehungen: {friendship_pairs}")
print(f"Freundschaften: {friendships}")
