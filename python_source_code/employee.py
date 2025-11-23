class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
        
    def showDetails(self):
        print("role =",self.role)
        print("department =",self.department)
        print("salary =",self.salary)


class Engineer(Employee):
    def __init__(self, name,age):
        # super().__init__("Engineer", "IT", "20000")
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT", "20000")

eng=Engineer("sandeep",22)
# eng.showDetails()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,price):
        return self.price > price.price
    
o1=Order("chips",20)
o2=Order("chocolate",35)
o3=o1>o2
print(o3)

