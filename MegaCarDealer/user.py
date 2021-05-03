class User:

    _userInstance=None
    

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if(User._userInstance == None):
            User()
        return User._userInstance

    def __init__(self,fname = None, lname = None, phone = None,address = None, email = None,password = None,role = None, uid=None):
        """ Virtually private constructor. """
        if User._userInstance != None:
            raise Exception("This class is a singleton!")
        else:
            
            self.id=uid
            self.fname = fname
            self.lname = lname
            self.phone = phone
            self.address = address
            self.email=email
            self.password=password
            self.role=role
            User._userInstance = self
    
    def getDataSet():
        return userDataSet
    
    def getId(self):
        return self.id

    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname 

    def getPhone(self):
        return self.phone

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getRole(self):
        return self.role
    
    def getPassword(self):
        return self.password

    def setId(self,uid):
        self.id=uid

    def setFirstName(self, fname):
            self.fname = fname

    def setLastName(self, lname):
            self.lname = lname

    def setPhone(self, phone):
            self.phone = phone

    def setAddress(self, address):
            self.address = address

    def setEmail(self, email):
            self.email = email

    def setRole(self, role):
            self.role = role

    def setPassword(self, password):
        self.password = password
    
    def setAttributes(self,attList):
        if(len(attList) == 8):
            self.setId(attList[0])
            self.setFirstName(attList[1])
            self.setLastName(attList[2])
            self.setPhone(attList[3])
            self.setAddress(attList[4])
            self.setEmail(attList[5])
            self.setPassword(attList[6])
            self.setRole(attList[7])
        else:
            print("Invalid Record for User!!")

# For Testing
# user1=User("HArry","Tank",2132143112,'asftysaf','ydtfwy','ewshrftgewyu',1)
# print(user1.getFirstName())
# print(user1.getPhone())
# print(user1.getRole())