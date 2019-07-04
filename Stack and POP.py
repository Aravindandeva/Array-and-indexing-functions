#Pushing into a sclass stack:
class stack :
  def __init__(self):
    self.stack=[]
  def add(self,dataval):
    if dataval not in self.stack:
      self.stack.append(dataval)
      return True
    else :
      return False

  def remove(self):
    if len(self.stack) <=0 :
      return ("No element in the Stack")
    else:
      return self.stack.pop()

a=stack()
a.add('enna ')
a.add('ennada')
a.add('solluda')
for i in (1,4):
  print(a.remove())
