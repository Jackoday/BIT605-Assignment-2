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

  starttime = time.time()
  def comb(n,r):
    x = fact(r+n-1)
    y = fact(r)
    z = fact(n-1)
    return (x/(y*z))
  print ("Combination of (" + str(n) + ", " + str(r) + ") = " + str(int(comb(n,r))))
  print ("Time: " + str((time.time()-starttime)*1000))

  starttime = time.time()
  def perm(n,r):
    if (r != 0):
      return (n * perm(n, r - 1))
    else:
        return 1;
  print ("Permutation of (" + str(n) + ", " + str(r) + ") = " + str(perm(n,r)))
  print ("Time: " + str((time.time()-starttime)*1000) + "\n") 

combPermRec(4,2)

#Combinations and permutations iterative
print ("Combinations and permutations - Iterative\n----------")
def combPermIt(n,r):

  starttime = time.time()
  def comb(n,r):

    a = (n+r-1)
    for i in range(a-1):
      a = a*((n+r-1)-(i+1))

    b = r
    for i in range(b-1):
      b = b*(r-(i+1))

    c = (n-1)
    for i in range(c-1):
      c = c*((n-1)-(i+1))

    return (a/(b*c))
  print ("Combinstion of (" + str(n) + ", " + str(r) + ") = " + str(int(comb(n,r))))
  print ("Time: " + str((time.time()-starttime)*1000))

  starttime = time.time()
  def perm(n,r):
    pow = 1
    for i in range (r):
      pow = pow * n
    return pow
  print ("Permutation of (" + str(n) + ", " + str(r) + ") = " + str(perm(n,r)))
  print ("Time: " + str((time.time()-starttime)*1000) + "\n")

combPermIt(4,2)


print ("\nBIT605 Assignment 2 part 2\n----------")

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
  for row in reader:
    list_unsorted.append(user(row[0], row[1], row[2], row[3])),
    reader.__next__

#Run bubble sort
bubbleList = list_unsorted
starttime = time.time()
bubbleSort(bubbleList)
print ("Time to sort data with bubble sort: " + str((time.time()-starttime)*1000))

#Run selection sort
selectionList = list_unsorted
starttime = time.time()
selectionSort(selectionList)
print ("Time to sort data with selection sort: " + str((time.time()-starttime)*1000))