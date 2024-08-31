# This contains code for Bubble Sort
## 1) Ineffcient Code
## 2) Efficient Code

````
# BUBBLE SORT

# SWAPPING VARIABLE
array =[9,0]
temp = array[0]
array[0]=array[1]
array[1]= temp
# there are two loops in bubble sort alorithm
# one inner loop means that one value is at the corrrect position
#and is responsible for swapping of each elements


# after one correct positioning of an element
# there will be another outer loop which basically determines
# the number of elements in array

# INEFFICIENT CODE
# USES BOTH FOR LOOPS AND PERFOMRS EXTRA UNWANTED LOOPS

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def bubblesort():
    for x in range(10):
        for y in range(0,9):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1]= temp
print(arrayData)
bubblesort()
print(arrayData)

print(8//3)

# EFFICIENT BUBBLE SORT

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def bubblesort():
     noswaps = False
     boundary = 9
     while noswaps == False:
         noswaps= True
         for y in range(0,boundary):
             if arrayData[y] > arrayData[y+1]:
                 temp = arrayData[y]
                 arrayData[y] = arrayData[y + 1]
                 arrayData[y + 1] = temp
                 noswaps = False
         boundary = boundary - 1
````
