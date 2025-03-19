class Student:
    
    def __init__(self,name,marks,marks1,marks2):
        self.name = name
        self.marks = marks
        self.marks1 = marks1
        self.marks2 = marks2

    def __pass__(self):
        print("YOUR PASS YOUR CLASS IS 10TH ", self.name,"Singh", "😎")    
        
s1 = Student(input("what is your Name: "),int(input("what is your marks: ")),int(input("what is your marks1: ")),int(input("what is your marks2: ")))

print(s1.name)
print(s1.marks)
print(s1.marks1)
print(s1.marks2)
s1.__pass__()

