friends = {0: {9, 7}, 1: {11, 4, 13, 39}, 2: {32, 33, 34, 3, 36, 10, 11, 29},
3: {2, 36, 37, 17, 19, 25, 26}, 4: {1, 36, 37, 8, 10, 20}, 5: {28, 31},
6: set(), 7: {0, 38, 10, 14, 21, 22, 28}, 8: {19, 4, 23}, 9: {0, 28},
10: {2, 4, 38, 7, 21}, 11: {1, 2, 35, 19, 24, 29}, 12: {24, 17, 34},
13: {32, 1, 20, 36}, 14: {36, 31, 7}, 15: {22}, 16: {37, 17, 19, 26, 27},
17: {32, 3, 35, 12, 16, 27, 29, 30}, 18: {32, 33, 37, 38, 20, 24, 26},
19: {3, 38, 8, 11, 16, 25}, 20: {33, 4, 36, 13, 18, 25, 29, 30},
21: {37, 38, 7, 10, 24}, 22: {36, 7, 15, 28, 29, 31}, 23: {8, 36},
24: {11, 12, 18, 21, 30}, 25: {3, 39, 19, 20, 27, 31}, 26: {32, 33, 3, 16, 18},
27: {38, 16, 17, 25, 28}, 28: {32, 5, 7, 9, 22, 27},
29: {33, 2, 37, 11, 17, 20, 22, 30}, 30: {33, 17, 20, 24, 29},
31: {25, 5, 22, 14}, 32: {2, 13, 17, 18, 26, 28}, 33: {2, 35, 18, 20, 26, 29, 30},
34: {2, 35, 12}, 35: {33, 34, 11, 17}, 36: {2, 3, 4, 39, 13, 14, 20, 22, 23},
37: {3, 4, 38, 16, 18, 21, 29}, 38: {37, 7, 10, 18, 19, 21, 27}, 39: {1, 36, 25}}

# function to derive the friends of friends from the list and returns a set of friends of friends
def friendsOfFriends(person:int, peopleDict:dict):
    """Find person's set of friends and their friends

    Parameters
    ----------
    person: int
        An integer representing a person
    peopleDict: dict
        A dictionary for a friendship network


    Returns
    -------
    A set of integers
    The set of the person's friends and their friends.

    """
    
    # getting the person and storing the key value in an empty set
    direct_friends = friends.get(person, set())
    friends_of_friends = set()
    
    # iterating through the keys to get their values and update the new set
    for i in direct_friends:
        friends_of_friends.add(i)
        friend = peopleDict.get(i,set())
        
        # updating the set for a certain direct friends with their friends
        friends_of_friends.update(friend)
        friends_of_friends.remove(person)
        
    return friends_of_friends
    
    
def test(friends_database):
    """Test friendsOfFriends()

    It prints out the sorted lists of friends and their friends for persons 0, 6 and 39.

    Parameters
    ----------
    friends_database : dict
        A friendship database

    Returns
    -------
    None
    """
    for person in [0,6,39]:
        list_friends = list(friendsOfFriends(person, friends_database))
        list_friends.sort()
        print("The person", str(person)+"\'s friends of friends are: ", list_friends)

    return

test(friends)