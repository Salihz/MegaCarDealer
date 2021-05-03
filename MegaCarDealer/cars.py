class Car:
    def __init__(self, carDetails):
        if(len(carDetails) == 0):
            self.id=None
            self.make = None
            self.model = None
            self.year = None
            self.color = None
            self.price = None
            self.quantity=None
        else:
            self.id=carDetails[0]
            self.make = carDetails[1]
            self.model = carDetails[2]
            self.year = carDetails[3]
            self.color = carDetails[4]
            self.price = carDetails[5]
            self.quantity=carDetails[6]

    def setCarId(self,id):
        self.id=id
    def getCarId(self):
        return self.id
    
    def setMake(self, make):
        self.make = make
    def getMake(self):
        return self.make
        
    def setModel(self, model):
        self.model = model
    def getModel(self):
        return self.model
        
    def setYear(self, year):
        self.year = year
    def getYear(self):
        return self.year
        
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
        
    def setPrice(self, price):
        self.price = price
    def getPrice(self):
        return self.price

    # def setCarId(self,id):
    #     self.car_id=id
    # def getCarId(self):
    #     return self.car_id

    def setCarQuantity(self,quantity):
        self.quantity=quantity
    def getCarQuantity(self):
        return self.quantity

    