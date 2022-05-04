import email
import string


class employee():

    def __init__(self,id,name,family,email,phone):
        self.id = id
        self.name = name
        self.family = family
        self.email = email
        self.phone = phone

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

emp = employee(1,"Javad","Bayzavi","email","1234567890")
print(emp.id)