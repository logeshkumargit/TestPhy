'''
Created on Apr 6, 2020

@author: logesh.kumar
'''
from _operator import contains
from Tools.demo.ss1 import colnum2name
from pip._internal.utils.misc import LOG_DIVIDER
from random import choice
from test.test_tools.test_unparse import for_else
print("I'm Python")

#List
courses =["1", "2","3"]
courses.append("4")
courses[0] = "0"
courses.insert(1, 1)
print(courses)

#Tuple
courses =("1", "2","3")
print(courses)

#set
courses1 = {"1","2","3","1","4","2"}
print(courses1)

#dictionary
dic = {'I':'India', 'G':'Germany'}
print(dic.__contains__('I'))


    
    
#For Loop
values = [1,2,3,4,5]
Add=0
for val in values :
    Add = Add+val
    print ("Addition:", Add)
    
#While Loop
Num = 10
Add=0
i=1
while i<=Num:
        Add = Add+i
        i=i+1
        print ("Addition:", Add)
    
    
    
    
#Addition
def Add(Num1, Num2):    
    return Num1+Num2
    
#subtract
def Sub(Num1, Num2):    
    return Num1-Num2

#multiply
def Multiply(Num1, Num2):    
    return Num1*Num2

#Divide
def Divide(Num1, Num2):    
    return Num1/Num2   

print("Select")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
Choose = input("Enter your choice")

Num1 = int(input("Enter first number:"))
Num2 = int(input("Enter second number:"))

if Choose == '1':
    print(Add(Num1,Num2))
    
elif Choose == '2':
    print(Sub(Num1,Num2))
    
elif Choose == '3':
    print(Multiply(Num1,Num2))
    
elif Choose == '4':
    print(Divide(Num1,Num2))
    



