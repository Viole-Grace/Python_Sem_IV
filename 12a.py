class city:
  def __init__(self,city,place=[]):
    self.city=city
    self.place=place

  def add_place(self,place):
    self.place.append(place)

  def remove_place(self,place):
    if place in self.place:
      self.place.remove(place)

  def display_place(self):
    print(self.place)
newCity=city(input("Enter a city: "))
while 1:
  print("\n1) Add a place")
  print("2) Remove a place")
  print("3) Display a place")
  print("4) End Program")
  choice=int(input("Enter Choice: "))
  if choice==1:
    newCity.add_place(input("Enter a place: "))
  elif choice==2:
    newCity.remove_place(input("Delete a place"))
  elif choice==3:
    newCity.display_place()
  elif choice==4:
    exit(0)