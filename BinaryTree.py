# Binary Tree
## **The following codes of Binary Tree are shared :**
#01 Adding Node in a Binary Tree\
#02 Searching in Binary Tree\
#03 PreOrder Traversal\
#04 InOrder Traversal\
#05 PostOrder Traversal

````

# BINARY TREE

#  A binary Tree is a type of data structure in which each node
#  has at most two children, referred to as the left child and the right
#  child. the nodes are arranged in a hierarchical structure, with a root
#  node at the top and the leaves at the bottom
# the top node is root
# the rootpointer points towards the location of the root
# each child  node can have a further family..and that node would be the root of his family


# ADDING A VALUE TO A BINARY TREE

# Always start comparing from the root
# if the value that you want to insert is bigger than the root then move right
# if the value is smaller than the root then move left
# VALUE > ROOT ----> RIGHT
# VALUE < ROOT  ----> LEFT


#   TREE TRAVERSAL

# tree traversal refers to the process of visiting and examining each
# node in a tree data structure in a specific order
# used when accessing nodes in a binary tree in a order

# 1) INORDER   2) PREORDER  3) POSTORDER

# 1) INORDER
# LEFT ROOT RIGHT

# 2) PREORDER
# ROOT LEFT RIGHT

# 3) POSTORDER
# LEFT RIGHT ROOT



# root = -
# right = a
# left = b
# if we have to access in this order "-ab" the use preoder




# check if there is space in binary tree
# check if root is empty. if yes then add value to the root
# if value is smaller than the root then move left
# now on left check is node is empty .if yes then add value

##                CREATING A 2D ARRAY FOR BINARY TREE

# arraynodes [C.P][0] = left pointer
# arraynodes [C.P][1] = data
# arraynodes [C.P][2] = right pointer


##  ADDING A NODE IN BINARY TREE

# First check if there is space in your binary tree or not by comparing the value
# of freenode if it has reached the max index then NO space
# then check if the root pointer is still pointing towards  -1 that means that there
# is no item in the binary tree and just change the value of root pointer to first index
# which  is 0.
# free node is the next empty space




#  ADDING A NODE IN BINARY TREE



ArrayNodes = [[0]*3 for x in range(20)]
RootPointer = -1
FreeNode = 0

def Addnode():
   global  ArrayNodes
   global RootPointer
   global FreeNode

   NodeData = int(input("enter the Data: "))

   # FIRST WE NEED TO CHECK THAT WE HAVE SPACE IN ARRAY OR NOT
   if FreeNode <= 19 :
      #FIRST CREATE A NODE AND INITIALIZE
      ArrayNodes[FreeNode][0] = -1 # left pointer of free node
      ArrayNodes[FreeNode][1] = NodeData # data of freenode
      ArrayNodes[FreeNode][2] = -1 # right pointer of freenode

      #FIRST CHECK DO YOU HAVE A ROOT VALUE .means is it empty or not
      if RootPointer == -1:
         RootPointer = 0
      else:
         Placed = False
         CurrentPointer = RootPointer
         # find the correct position and adjust the pointers
         while Placed == False:
            # IF it is smaller value so go left
            if NodeData < ArrayNodes[CurrentPointer][1]:
               # need to check first if it empty or not
               # if it is empty means -1 then just store
               # otherwise increment
               if ArrayNodes[CurrentPointer][0] == -1:
                  ArrayNodes[CurrentPointer][0] = FreeNode
                  Placed = True
               else:
                  CurrentPointer = ArrayNodes[CurrentPointer][0] # increment

            else:
                  # this else if if the value is greater than the root
                  # so i should move towards right side or check if it is empty
                  if ArrayNodes[CurrentPointer][2] == -1 :
                     ArrayNodes[CurrentPointer][2] = FreeNode
                     Placed = True
                  else:
                     # then increment right
                     CurrentPointer= ArrayNodes[CurrentPointer][2]

      FreeNode = FreeNode + 1
   else:
      print("Tree if Full")


# SEARCHING IN BINARY TREE

def FindNode(searchitem):
   global RootPointer
   global ArrayNodes

   CurrentPointer = RootPointer

   # WHILE LOOP FOR SEARCHING PURPOSE
   while CurrentPointer != -1 and ArrayNodes[CurrentPointer][1] != searchitem:
      if searchitem < ArrayNodes[CurrentPointer][1]:
         CurrentPointer = ArrayNodes[CurrentPointer][0]

      else:
         CurrentPointer = ArrayNodes[CurrentPointer][2]

   print(CurrentPointer)


Addnode()
Addnode()
Addnode()

print("Root pointer ", RootPointer)
print("Free node", FreeNode)

for x in range(20):
   print(ArrayNodes[x])

FindNode(30)




#  Tree Travserals

FreeNode = 6
RootPointer = 0

BinaryTree = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]


# INORDER
def Inorder(Root):
   global BinaryTree
   if BinaryTree[Root][0] != -1:
      Inorder(BinaryTree[Root][0])
   print(BinaryTree[Root][1])

   if BinaryTree[Root][2] != -1:
      Inorder(BinaryTree[Root][2])


Inorder(RootPointer)

# PRE ORDER

def PreOrder(Root):
   global BinaryTree
   print(BinaryTree[Root][1])
   if BinaryTree[Root][0] != -1 :
      PreOrder(BinaryTree[Root][0])
   if BinaryTree[Root][2] != -1 :
      PreOrder(BinaryTree[Root][2])


# POST ORDER

def PostOrder(Root):
   if BinaryTree[Root][0] != -1 :
      PostOrder(BinaryTree[Root][0])
   if BinaryTree[Root[2]] != -1:
      PostOrder(BinaryTree[Root][2])
   print(BinaryTree[Root][1])




# Question 3 winter 2022 p42

# DECALRE ArrayNodes : ARRAY[0:19,0:2] OF INTEGER

ArrayNodes = []
for x in range(20):
   ArrayNodes.append([-1,-1,-1])

ArrayNodes[0][0] = 1
ArrayNodes[0][1] = 20
ArrayNodes[0][2] = 5
ArrayNodes[1][0] = 2
ArrayNodes[1][1] = 15
ArrayNodes[1][2] = -1
ArrayNodes[2][0] = -1
ArrayNodes[2][1] = 3
ArrayNodes[2][2] = 3
ArrayNodes[3][0] =-1
ArrayNodes[3][1] = 9
ArrayNodes[3][2] = 4
ArrayNodes[4][0] = -1
ArrayNodes[4][1] = 10
ArrayNodes[4][2] = -1
ArrayNodes[5][0] = -1
ArrayNodes[5][1] = 58
ArrayNodes[5][2] = -1
RootPointer = 0
FreeNode = 6

print(ArrayNodes)


# CODE OF SEARCHING IN BINARY TREE  USING RECURSION
def SearchValue(Root, Valuetofind):
   global ArrayNodes

   if Root == -1:
      return -1
   elif ArrayNodes[Root][1] == Valuetofind:
      return Root
   elif  ArrayNodes[Root][1] == -1:
      return -1

   if ArrayNodes[Root][1] > Valuetofind:
      return SearchValue((ArrayNodes[Root][0]),Valuetofind)

   if ArrayNodes[Root][1] < Valuetofind:
      return SearchValue(ArrayNodes[Root][2],Valuetofind)


def PostOrder(Root):
   global ArrayNodes


   if ArrayNodes[Root][0] != -1:
      PostOrder(ArrayNodes[Root][0])
   if ArrayNodes[Root][2] != -1:
      PostOrder(ArrayNodes[Root][2])
   print(ArrayNodes[Root][1])

temp  = SearchValue(RootPointer,15)
if temp == -1 :
   print("the value was not found")
else:
   print("the value was found to be at" + " " + str(temp))
PostOrder(RootPointer)




ArrayNodes = [[0]*3 for x in range(20)]
RootPointer = -1
FreeNode = 0


def Addnode():
   global RootPointer
   global FreeNode
   global ArrayNodes

   datainput = int(input("Enter value"))
   if FreeNode <=19:
      ArrayNodes[FreeNode][0] = -1
      ArrayNodes[FreeNode][1] = datainput
      ArrayNodes[FreeNode][2] = -1

      if RootPointer == -1:
         RootPointer = 0
      else:
         placed  = False
         currentpointer = RootPointer
         while placed == False:

            if datainput < ArrayNodes[currentpointer][1]:
               if ArrayNodes[currentpointer][0] == -1:
                  ArrayNodes[currentpointer][0] = FreeNode
                  placed = True
               else:
                  currentpointer = ArrayNodes[currentpointer][0]
            else:
               if ArrayNodes[currentpointer][2] == -1:
                  ArrayNodes[currentpointer][2] = FreeNode
                  placed = True
               else:

                  currentpointer = ArrayNodes[currentpointer][2]

         FreeNode = FreeNode + 1
   else:
      print("tree is full")


def Finditem(item):
   global ArrayNodes
   global FreeNode
   global RootPointer

   currentpointer = RootPointer

   while currentpointer != -1 and ArrayNodes[currentpointer][1] != item:
      if item < ArrayNodes[currentpointer][0]:
         currentpointer = ArrayNodes[currentpointer][0]
      elif item > ArrayNodes[currentpointer][2]
         currentpointer = ArrayNodes[currentpointer][2]

````
