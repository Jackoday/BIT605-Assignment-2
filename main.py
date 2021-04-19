# Tower of Hanoi recursive
print ("Tower of Hanoi recursive\n----------")
def TowerOfHanoiR(n , fromPeg, aux, toPeg):
  if n==1:
    print ("Move disk 1 from",fromPeg,"to",toPeg)
    return
  TowerOfHanoiR(n-1, fromPeg, toPeg, aux)
  print ("Move disk",n,"from",fromPeg,"to",toPeg)
  TowerOfHanoiR(n-1, aux, fromPeg, toPeg)

TowerOfHanoiR(3,'A','B','C') 
print("\n")

# Tower of Hanoi iterative
print ("Tower of Hanoi iterative\n----------")
def TowerOfHanioI(n , fromPeg, aux, toPeg):
  maxMoves = pow(2,n)-1
  i = 1
  for i in range (i,(maxMoves+1)):
    source = (i & i-1)%3
    target = ((i | i-1)+1)%3

    if ((n%2) != 0):
      
      if(source == 0):
        fromPeg = "A"
      elif(source == 1):
        fromPeg = "B"
      else:
        fromPeg = "C"

      if(target == 0):
        toPeg = "A"
      elif(target == 1):
        toPeg = "B"
      else:
        toPeg = "C"

    elif((n%2)==0):

      if(source == 0):
        fromPeg = "A"
      elif(source == 1):
        fromPeg = "C"
      else:
        fromPeg = "B"

      if(target == 0):
        toPeg = "A"
      elif(target == 1):
        toPeg = "C"
      else:
        toPeg = "B"
    
    print("Move disk",n,"from",fromPeg,"to",toPeg)

TowerOfHanioI(3,'A','B','C')
print("\n")