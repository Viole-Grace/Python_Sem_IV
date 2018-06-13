class QEmpty(Exception):
  pass
class QFull(Exception):
  pass
class QUEUE():
  q=[]
  def __init__(self,size):
    self.size=size
  def insert(self,data):
    if len(QUEUE.q) > size:
      raise QFull
    else:
      self.data=data;
      QUEUE.q.append(self.data)
  def delete(self):
    if len(QUEUE.q) == 0:
      raise QEmpty
    else:
      print "Removed element : ",QUEUE.q.pop(0)
  def display(self):
    print QUEUE.q
size=int(raw_input("Enter queue size : "))
try:
  while True:
    ch=int(raw_input("Enter your choice : \n1.Insert into Queue\n2.Delete element from Queue\n3.Display Queue\n"))
    obj=QUEUE(size);
    if ch==1:
      val=int(raw_input("Enter value you want to insert : "))
      obj.insert(val)
    elif ch==2:
      obj.delete()
    elif ch==3:
      obj.display()
    else:
      break
except QEmpty:
  print "Queue is Empty -- "
except QFull:
  print "Queue is Full -- Cannot insert any more elements!"