class Student():
    count=0
    pycount=0
    def __init__(self,USN,Name,Subject):
        self.USN=USN
        self.Name=Name
        self.Subject=Subject
        if self.Subject.lower()=="python":
            Student.pycount+=1
        Student.count+=1
listofstud=[]
n=int(input("Enter the number of students "))
for i in range(n):
    name=input("Enter Name ")
    usn=input("Enter USN ")
    sub=input("Enter Subject ")
    result=Student(usn,name,sub)
    listofstud.append(result)
for i in listofstud:
    if i.Subject.lower()=="python":
      print (i.Name,"Has taken Python")
print (Student.pycount,"Have taken Python")
