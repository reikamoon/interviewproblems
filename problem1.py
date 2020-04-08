#Data Structure I will use: Set
List = [1, 2, 3, 4, 4, 5]
Set = {1, 2, 3, 4, 4, 5} #< --- I turned the list into a set
#Another way would be Set(list).
# Given a list of an unspecified number of numbers, determine if the list has a duplicate number.
#
# Questions:
# How many numbers are there?
# Are the numbers integers or strings?

def find_the_dup(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True

# Time Complexity: O(1), because it only goes through each element once.

if __name__ == '__main__':
    list = [1, 2, 3, 4, 4, 5]
    result = find_the_dup(list)

    if result:
        print('List does contain duplicates.')
    else:
        print("No duplicates found in the list.")
