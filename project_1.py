#Python Hack w/ Cam 'n' Phil - 2024
#1- create 2 arrays, array1 with all the characters of the alphabet, array2 21 numbers, from 0 to 20 
#2- Create a function to randomly mix the alphabet characters in array1 
#3- Create a function to add number to array2, add numbers 21 to 1000 

import random

def addNum(num, inputList):
    inputList.append(num)
    
def augmentList(num, inputList):
    for i in range(len(inputList), num + 1):
        addNum(i, inputList)
            
def shuffleList(inputList):
    random.shuffle(inputList)

numbers = [0,1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(alpha)
print (numbers)

shuffleList(alpha)
print(alpha)

augmentList(100, numbers)
print (numbers)