class QueueFullError(Exception):     
   pass 
class QueueEmptyError(Exception):     
   pass 
class MyQueue:     
  def __init__(self,size):         
    self.items = []*(size)         
    self.size=size-1     
  def INSERT(self, item):       
      try:         
        if(len(self.items)<=self.size):             
          self.items.insert(0,item)         
        else:             
          raise QueueFullError       
      except QueueFullError:           
        print("queue is full") 
  def DELETE(self):         
      try:             
        if(len(self.items)>0):                
           return self.items.pop()    
        else:                 
            raise QueueEmptyError 
      except QueueEmptyError:             
        print("queue is empty")     
  def DISPLAY(self):         
      print(self.items) 
t=int(input("upper bound of array")) 
q=MyQueue(t) 
print("1.insert\n2.delete\n3.display\n4.quit") 
while(1):     
    n=int(input("enter choice"))     
    if(n==1):         
      x=int(input("enter element"))         
      q.INSERT(x)     
    elif(n==2):         
      q.DELETE()     
    elif(n==3):
      q.DISPLAY()
    elif(n==4):
      exit(0)
