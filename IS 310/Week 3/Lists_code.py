"""
Module - Lists and Tuples
@author: prs
"""

#Lists are mutable, meaning the values inside them can be changed and/or overwritten
#Lists are dynamic, so we can add, subtract, append to them, and so on
def UnderstandingLists():
    myList = [5,6,7,8,9]    

    myList2 = ['Sally', 'Lucy', 'Mike']
    
    myList3 = [1, 4.657, 'Daniel']    


    print(f'{myList}\n{myList2}\n{myList3}')
    
    print('\n--------------------------------')
        
    rangeList = list(range(5))
    rangeList_2 = list(range(10, 1, -2))
    
    print(f'{rangeList}\n{rangeList_2}')
    print('\n--------------------------------')
    
    listCopies = [1,2,3,'Copy'] * 5
    
    print(listCopies)
    print('\n--------------------------------')
 
## -------------------------------------------------------- ##

def LoopingLists():
    
    numbers = [1,2,3,4,7,10]
        
    for values in numbers:
        print(values)
        
    print('\n')
    
    for values in numbers:
        
        if values % 2 == 0:
            
            print("even")
            
        else:
            
            print("odd")
        
        
    print('\n---------------------------------')
    
    print(numbers[0], numbers[4])
    #this will give us an index out of range or index out of bounds error
    #print(numbers[6])
    
## -------------------------------------------------------- ##

def LenFunction():
    
    numbers = [5, 9, 10, 456, 23, 8]
    
    length = len(numbers)
    print(length)
    print(numbers[5])

## -------------------------------------------------------- ##

def Mutability():
    
    numbers = [5, 9, 10, 456, 23, 8]
    
    numbers[3] = 18
    
    print(numbers)

## -------------------------------------------------------- ##

def ConcatenateLists():
    
    myList_1 = [1, 2, 3, 4]
    myList_2 = [5, 6, 7, 8]
    
    result = myList_1 + myList_2
    
    print(result)
    
    print('\n--------------------------------')
    
    mtypesList = [1, 4.5, 'Sally']
    mtypesList2 = ['John']
    
    result = mtypesList + mtypesList2
    
    print(result)

## -------------------------------------------------------- ##

def ListSlicing():
    
    numbers = [ 5, 9, 14, 25, 40, 55]
    
    last_half = numbers[3:6]
    print(last_half)
    
    first_half = numbers[0:3]
    print(first_half)
    
    from_to_end = numbers[2:]
    print(from_to_end)
    
    skipping = numbers[2:6:2]
    print(skipping)
    
    newList = skipping + first_half
    print(newList)

## -------------------------------------------------------- ##

## -------------------------------------------------------- ##

def AppendLists():
    
    listA = [0, 1, 2, 3, 4, 5]
    
    i = 6
    for number in range(0, 3):
    
        listA.append(i)
        i += 1
    
    print(listA)

## -------------------------------------------------------- ##

def InsertLists():
    
    listB = [0, 1, 2, 3, 5, 6, 7]
    
    listB.insert(4, 4.567)
    listB.insert(2, 90)
    
    #listB.remove(5)
    
    print(listB)

## -------------------------------------------------------- ##
 
def SortingLists():
    
    unsortedList = [10, 0, 4, 8, 16, 1, 2]
    
    unsortedList.sort()
    
    ascendingSort = unsortedList
    
    print(ascendingSort)
    
    ascendingSort.reverse()
    
    descendingSort = ascendingSort
    
    print(descendingSort)    

## -------------------------------------------------------- ##

def twoDimensionalLists():
    
    studentScores = [['Greg', 100, 90 ], ['Veronica', 96, 88], ['Gandalf', 100, 100]]
    
    print(studentScores[0])
    print(studentScores[1])
    print(studentScores[2])
    
    for rows in studentScores:
        
        print('\n')
        for elements in rows:
            
            print(f'{elements}')

## -------------------------------------------------------- ##

def UnderstandingTuples():
    myTuple = (9,5,10,0,1,3)
    
    for numbers in myTuple:
        
        print(numbers)
    
    #Cannot do these: --------------
    #myTuple.append(6)
    #myTuple.insert(2,18)
    #myTuple.remove(0)
    #myTuple.sort()
    #myTuple.reverse()
    
    newTuple= myTuple[2:5]
    print(newTuple)
    #print(myTuple)
    
    myTuple2 = (10, 11)
    
    myTuple = myTuple2
    
    print(myTuple)
    
    myTuple3 = myTuple + myTuple2
    
    print(myTuple3)
     
    value = 10
    if value in myTuple:
        
        print(f'10 was found at {myTuple.index(value)}')
        
    else:
        
        print("10 was not found")

## -------------------------------------------------------- ##

def Immutability():
    
    numbers = (5, 9, 10, 456, 23, 8)
    
    numbers[3] = 18
    
    print(numbers)
    
if __name__=='__main__':
    #UnderstandingLists()
    #LoopingLists()
    #LenFunction()
    #Mutability()
    #ConcatenateLists()
    #ListSlicing()
    #AppendLists()
    #InsertLists()
    #SortingLists()
    #twoDimensionalLists()
    #UnderstandingTuples()
    #Immutability()