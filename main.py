import numpy as np
from src.utils.listmanipulator import ListPracticer

def practiceDataStructures():
    """
    This function is for initiation of different practice functions for different 
    data structures

    1. List (Why, How and Where to Use)
    2. Tuples (Why, How and Where to Use)
    3. Dictionaries (Why, How and Where to Use)
    4. Sets (Why, How and Where to Use)
    5. Strings (Why, How and Where to Use)
    
    """

def multiply(x):
    return x**2

def main_function():
    """
    This is main function
    """
    # listObj = ListPracticer(1)
    # listObj.getinfolist()

    # List creation practice
    # Way #1
    mylist1 = [1,56,3]



    # print (mylist1, mylist1.__add__([5]))
    # print(mylist.__reversed__.__doc__)

    # print(mylist1*3) # +,-,/ Doesn't work on list but * creates copy of elements in original list

    # print(mylist1.index(2))
    # print(mylist1.count)

    print("-------------------------Looping------------------------")
    # Looping: Way#1 
    # for i in mylist1:
    #     print(i)

    # Looping: Way#2 
    # for index, value in enumerate(mylist1):
    #     print(index, value)
    #     if index%2 ==0 and index!=0:
    #         index = index - 1

    print("-------------------------Looping------------------------")

    # Looping: Way#3
    # for i in range(0,5):
    #     print('Row Value: ',i)
    #     if i%3 == 0:
    #         i -=1
    #         print('Condition True, i decremented')
    #     for j in range(0,len(mylist1)):
    #         print('Column Value: ',j)

    # Nested Looping: 

    # for i in range(10):
    #     if i == 5:
    #         continue
    #     for j in range(10):
    #         print(f"i = {i}, j = {j}")

    # mylist1.extend(['12','3'])
    # mylist1.clear()
    # mylist1.pop(1)
    # mylist1.reverse()
    # mylist1 = list(reversed(mylist1)) //Not inplace sorting, built in fucntion of python
    # mylist1.sort() //Inplace sorting, method of list

    # ------------------------------------usage of builtin functions-------------------------

    # mylist1 = [2 * x for x in mylist1]

    x = np.array([1,2,3])
    print(x)
    # mylist1 = map(multiply,mylist1) // MAP function is used to apply function on iterable 
    # objects (List, String, Tuples).



    print(mylist1)


x = [1,54,2,7,3]

def checkNumber(x):
    return x<2

# y = list(filter(checkNumber, x)) // this filter builtin function works on
# iterable object and filters results which meets condition

# y = list(filter(lambda i: i<2 , x))

print(min(y))


# if __name__ == '__main__':
#     main_function()