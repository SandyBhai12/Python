# class Student:
#     def __init__(this,fullname):
#            this.fullname=fullname
           
#            print("yeah Students how are you")

# s1=Student("Sandeep")
# print(s1.fullname)


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def showDetails(self):
        for i in self.marks:
            print("Name of the student is :- ",self.name," and marks of three subjects are => ",i)

    def avgMarks(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi ",self.name," your avg marks is = " ,sum//3)

    @staticmethod
    def hello():
        print("hello boss")



s1=Student("sandeep",[30,40,50])
s1.avgMarks()
s1=Student("akash",[89,30,86])
s1.avgMarks()
s1=Student("paroo",[8,3,86])
s1.avgMarks()
s1.hello()
