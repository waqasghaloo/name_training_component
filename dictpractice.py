import numpy as np
from collections import defaultdict

grid = [
             ["B","B","B"],
             ["B","B","E"],
             ["E","E","B"],
             ["E","E","E"],
             ["B", "E", "B"]
             ]

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "B":
        return
    grid[i][j] = "V"
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)

def countBuildings(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "B":
                count += 1
                dfs(grid, i, j)
    return count
print(countBuildings(grid))


# {
#     1: [0,1], [0,2], []

# }

# buildingDict = {}
# When you want to create a dictionary and you know what will be type of value 
# but you are not of values to be inserted in start, use defaultdict(list) to create a dictionary
# so you can append list later on.

# building = {1:[1,2]}
# building = [key: [] for key in keys]

# print(help(dict.fromkeys))
b=dict.fromkeys([1,2,3], list)
print(b)
# buildingDict = defaultdict(list)

# minRowIter = 0
# maxRowIter = len(buildings)

# minColIter = 0
# maxColIter = len(buildings[0]) 
# dictKey = 0

# for row in range(minRowIter, maxRowIter):
#     for col in range(minColIter, maxColIter):
        
#         if buildings[row][col] == "B":
#             buildingDict[dictKey].append([row,col])
#         elif buildings[row][col] == "E":
            

# print(buildingDict) 







# print(dir(buildings))
# print(buildings.__delitem__.__doc__)
# print(help(buildings.__delitem__))


# ----------------------------Dictionary Creation--------------------------
# Way#1 creating a dictionary of strings with parentheses approach 
# d = {1: 'Hi', 2:'Hello'}

# # Way#2 creating a dictionary of lists with comprehension approach
# d1 = {key : [] for key in [1,2,3]}


# # Way#3 Creating a dictionary with iterable object as keys and value using built in type 'dict'
# # and method of class fromkeys
# d2 = dict.fromkeys([1,2,3])
# print(d2)


# # ---------------------------Accessing Dictionary-------------------------
# # way #1 to access dictionary using square brackets
# print(d[1])

# # way #2 to access dictionary using get method, with get method if value is not
# # available it won't raise an error but a default value
# print(d.get(3)) 


# Way #3 to access dictionary of list 
# Note : Dictionaries works with keys not indexes


# -----------------------------Adding Element in Dictionary-------------------
# d = {key : [] for key in [1,2,3]}

# d[1].append(["B","C"]) # This is append another list at key 1

# d[1].extend(["B","C"]) # This will extend existing list by adding values to it.
# print(d) 

# -----------------------------Deleting Element from Dictionary-------------------
# d.clear() # To clear all from dictionary d
# d[1].clear() # To delete value at key 1 
# d[1].pop() # This will pop last element from set of value  at end [] 
# print(d) 

# print(list(d.keys())) #This approach will cast existing datatype to list
# print([d.keys()]) #This approach will put element inside list


# print(d.values()) dict_values(['Hi', 'Hello'])
# print(d.items()) dict_items([(1, 'Hi'), (2, 'Hello')])
# print(d.keys()) dict_keys([1, 2])


# ----------------------------------- Iteration on dictionary -------------------
# Way #1

# for key, values in d.items():
#     print(f'{key}:')
#     for value in values:
#         print(value)


# Way #2

# import itertools

# d = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}
# for value in itertools.chain(*d.values()):
#     print(value)