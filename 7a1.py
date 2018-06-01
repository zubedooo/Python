from sample import stack
print("Empty Stack")
print(stack.GetStack())
print("1.Push\n2.Pop\n3.Is Empty\n4.Top")
while 1:
  n=int(input("Enter Your Choice"))
  if(n==1):
    item=input("Enter Element: ")
    stack.push(item)
  if(n==2):
    print(stack.pop())
  if(n==3):
    print(stack.isEmpty())
  if(n==4):
    print(stack.top())
  if(n==-1):
    break   