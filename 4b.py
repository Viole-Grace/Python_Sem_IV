class Adder:
  def add(self,x,y):
    print("Not Implemented")
  def __init__(self,start=[]):
    self.data=start
  def __add__(self,other):
    self.data+=other
    print(self.data)
  def __radd__(self,other):
    return self.add(self.data,other)

class listadder(Adder):
  def add(self,x,y):
    return x+y
class dictadder(Adder):
  def add(self,x,y):
    new={}
    for k in x.keys():
      new[k]=x[k]
    for k in y.keys():
      new[k]=y[k]
    return new
x=Adder()
print(x.add(1,2))
x=listadder()
print(x.add([1],[2]))
x=dictadder()
print(x.add({"a":"1"},{"b":"2"}))
x=Adder([1])
print(x+[3])
x=listadder([1])
print(x+[8])
print([2]+x)