class MarksNotElligibleError(Exception):
  pass
class NotValidIntergerError(Exception):     
  pass
try:     
  l=[]     
  for i in range(3):         
        t=int(input("Enter Marks for a subject"))         
        l.append(t)         
        if(t>50 or t<0):             
          raise NotValidIntergerError         
        if(t<20):             
          raise MarksNotElligibleError
except MarksNotElligibleError:     
  print("marks not elligible") 
except NotValidIntergerError:     
  print("entered marks is not a valid integer")
