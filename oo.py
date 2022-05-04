import email
import string


class employee:

    #def __init__(self,id,name,family,email,phone) -> None:
        #self.id = 1
       # self.name = "Javad"
        #self.family = "Bayzavi"
       # self.email = "javadbayzavi@gmail.com"
       # self.phone = "+989173098261"

# Getter and Setter for class property
    #@property
    def getId(self):
        return self.id
    def setId(self,value):
        self.id = value
    
    id = property(getId,setId)

    @property
    def Name(self):
        self.name
    def Name(self,value):
        self.name = value

#emp = employee(1,"Javad","Bayzavi","email","1234567890")
emp = employee()
emp.id = 12
emp.name = "Javad"
print(emp.name)