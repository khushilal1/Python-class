# Class/Static Variables
# Class for Computer Science Student
class CSStudent:
    stream = 'cse' # Class Variable or global variable
    def __init__(self,name,roll):
        self.name = name # Instance Variable
        self.roll = roll # Instance Variable
# Objects of CSStudent class
a = CSStudent('mohan', 6541)
b = CSStudent('student2', 2)
# print(a.stream)      # prints "cse"
# print(b.stream) # prints "cse"
# print(a.name) # prints "student1"
# print(b.name) # prints "student2"
# print(b.roll) # prints "2"
# print(a.roll) # prints "1"
# print(CSStudent.stream)


#chanf=gin e valu of a only 
a.stream="computer"
print(a.stream)
print(b.stream)

#changing for b only
b.stream="math"
print(a.stream)
print(b.stream)


#changingb for both a and b
CSStudent.stream="mechanical"
print(a.stream)
print(b.stream)
