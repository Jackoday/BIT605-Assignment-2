import time
import csv

print ("BIT605 Assignment 2 part 1\n----------\n")

#Tower of Hanoi recursive
print ("Tower of Hanoi - Recursive\n----------")
def towerOfHanoiR(n , fromPeg, aux, toPeg):
  if n==1:
    print ("Move disk 1 from",fromPeg,"to",toPeg)
    return
  towerOfHanoiR(n-1, fromPeg, toPeg, aux)
  print ("Move disk",n,"from",fromPeg,"to",toPeg)
  towerOfHanoiR(n-1, aux, fromPeg, toPeg)

starttime = time.time()
towerOfHanoiR(3,'A','B','C') 
print ("Time: " + str((time.time()-starttime)*1000) + "\n")

#Tower of Hanoi iterative
print ("Tower of Hanoi - Iterative\n----------")
def towerOfHanioI(n , fromPeg, aux, toPeg):
  maxMoves = pow(2,n)
  pegA = []
  pegB = []
  pegC = []
  movedDisk = 1
  for i in range(n):
    pegA.append(i+1)
  for i in range (1,(maxMoves)):
    source = (i & i-1)%3
    target = ((i | i-1)+1)%3

    if ((n%2) != 0):
      
      if(source == 0):
        fromPeg = "A"
        movedDisk = pegA[0]
        pegA.pop(0)
      elif(source == 1):
        fromPeg = "B"
        movedDisk = pegB[0]
        pegB.pop(0)
      else:
        fromPeg = "C"
        movedDisk = pegC[0]
        pegC.pop(0)

      if(target == 0):
        toPeg = "A"
        pegA.insert(0,movedDisk)
      elif(target == 1):
        toPeg = "B"
        pegB.insert(0,movedDisk)
      else:
        toPeg = "C"
        pegC.insert(0,movedDisk)

    elif((n%2)==0):

      if(source == 0):
        fromPeg = "A"
        movedDisk = pegA[0]
        pegA.pop(0)
      elif(source == 1):
        fromPeg = "C"
        movedDisk = pegC[0]
        pegC.pop(0)
      else:
        fromPeg = "B"
        movedDisk = pegB[0]
        pegB.pop(0)

      if(target == 0):
        toPeg = "A"
        pegA.insert(0,movedDisk)
      elif(target == 1):
        toPeg = "C"
        pegC.insert(0,movedDisk)
      else:
        toPeg = "B"
        pegB.insert(0,movedDisk)
    
    print("Move disk",movedDisk,"from",fromPeg,"to",toPeg)

starttime = time.time()
towerOfHanioI(3,'A','B','C')
print ("Time: " + str((time.time()-starttime)*1000) + "\n")

#Combinations and permutations recursive
print ("Combinations and permutations - Recursive\n----------")
def combPermRec(n,r):

  def fact(n):
    if (n <= 0):
      return 1
    else:
      return n * fact(n-1)

  def comb(n,r):
    x = fact(r+n-1)
    y = fact(r)
    z = fact(n-1)
    return (x/(y*z))
  print ("Combination of (" + str(n) + ", " + str(r) + ") = " + str(int(comb(n,r))))

  def perm(n,r):
    if (r != 0):
      return (n * perm(n, r - 1))
    else:
        return 1;
  print ("Permutation of (" + str(n) + ", " + str(r) + ") = " + str(perm(n,r)))

starttime = time.time()
combPermRec(4,2)
print ("Time: " + str((time.time()-starttime)*1000) + "\n")

#Combinations and permutations iterative
print ("Combinations and permutations - Iterative\n----------")
def combPermIt(n,r):

  #def comb(n,r)

  def perm(n,r):
    pow = 1
    for i in range (r):
      pow = pow * n
    return pow
  print ("Permutation of (" + str(n) + ", " + str(r) + ") = " + str(perm(n,r)))

starttime = time.time()
combPermIt(4,2)
print ("Time: " + str((time.time()-starttime)*1000) + "\n")


print ("\nBIT605 Assignment 2 part 2\n----------\n")

class user:
  def __init__(self, ID, fName, lName, email):
    self.ID = int(ID)
    self.lName = lName
    self.fName = fName
    self.email = email

def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j].lName > arr[j+1].lName :
        arr[j], arr[j+1] = arr[j+1], arr[j] 

def selectionSort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[min_idx].lName > arr[j].lName:
        min_idx = j           
    arr[i], arr[min_idx] = arr[min_idx], arr[i] 

#import unsorted list
list_unsorted = []
with open("BIT605_unsorted_data.csv") as csv_file:
  reader = csv.reader(csv_file, delimiter=",")
  for i in list(csv_file):
    list_unsorted.append(user((i.rsplit(',')[0]), (i.rsplit(',')[2]), (i.rsplit(',')[1]), (i.rsplit(',')[3])))

#Run bubble sort
bubbleList = list_unsorted
starttime = time.time()
bubbleSort(bubbleList)
print ("Time to sort data with bubble sort: " + str((time.time()-starttime)*1000) + "\n")

#Run selection sort
selectionList = list_unsorted
starttime = time.time()
selectionSort(selectionList)
print ("Time to sort data with selection sort: " + str((time.time()-starttime)*1000) + "\n")

#Binary Search Tree
class BSTNode:
  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val

  def insert(self, val):
    if not self.val:
      self.val = val
      return

    if self.val == val:
      return

    if val < self.val:
      if self.left:
        self.left.insert(val)
        return
      self.left = BSTNode(val)
      return

    if self.right:
      self.right.insert(val)
      return
    self.right = BSTNode(val)

  def get_min(self):
    current = self
    while current.left is not None:
      current = current.left
    return current.val

  def get_max(self):
    current = self
    while current.right is not None:
      current = current.right
    return current.val

  def preorder(self, vals):
    if self.val is not None:
      vals.append(self.val)
    if self.left is not None:
      self.left.preorder(vals)
    if self.right is not None:
      self.right.preorder(vals)
    return vals

  def inorder(self, vals):
    if self.left is not None:
      self.left.inorder(vals)
    if self.val is not None:
      vals.append(self.val)
    if self.right is not None:
      self.right.inorder(vals)
    return vals

  def exists(self, val):
    if val == self.val:
      return True

    if val < self.val:
      if self.left == None:
        return False
      return self.left.exists(val)

    if self.right == None:
      return False
    return self.right.exists(val)

def height(root):
  #if root is None return 0
    if root==None:
      return 0
    #find height of left subtree
    hleft=height(root.leftChild)
    #find the height of right subtree
    hright=height(root.rightChild)  
    #find max of hleft and hright, add 1 to it and return the value
    if hleft>hright:
      return hleft+1
    else:
      return hright+1

bst = BSTNode()
for user in list_unsorted:
  bst.insert(user.ID)

print("Number exists:")
print(bst.exists(647))

print(height())

print(bst.inorder([]))