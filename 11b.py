def subsetSum(ls, target):
  pos = 0
  if target in ls:
    return True
  while pos<len(ls) and ls[pos]<=target:
    pos+=1
    for i in range(pos+1):
      for j in range(i):
        for k in range(j):
          try:
            if ls[i]+ls[j]+ls[k]==target:
              return True
          except:
            return False
  return False
print("Enter a list of numbers: ")
ls = list(map(int, input().split()))
print("Enter the target: ")
target = int(input())
ls.sort()
print(subsetSum(ls, target))
