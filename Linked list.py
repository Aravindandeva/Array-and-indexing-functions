class Node :
  def __init__(self,dataval=None):  
    self.dataval=dataval
    self.nextval=None
    self.prevval=None

class SLinkedList:
  def __init__(self):
    self.headval=None

  def listprint(self):
    printval=self.headval
    while printval is not None:
      print(printval.dataval)
      printval=printval.nextval

list=SLinkedList()
list.headval=Node("Mon")
e2=Node("tue")
e3=Node("wed")
#Linking next value to the initial node
list.headval.nextval=e2
list.headval.nextval=e3


