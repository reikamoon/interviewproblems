#Data Structure I will use: Set
List: (1, 2, 3, 4, 4, 5)
Set = {1, 2, 3, 4, 4, 5} #< --- I turned the list into a set
#Another way would be Set(list).

def find_the_dup(list, set):
“””Check if list has duplicates by comparing to set”””
If len(list) === len(set): #Another way would be if len(list) == len(set(list)):
Print (“Duplicate found!”)
Return true
Else
print(“No Duplicates found :L”)
Return false
