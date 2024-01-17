class Transport:
    def __init__(self,Brand:str,Model:str,Color:str):
        self.Brand=Brand
        self.Model=Model
        self.Color=Color
    def getInfo(self):
            return f'''
Brand:{self.Brand}
Model:{self.Model}
Color:{self.Color}
    '''
class Car(Transport):
    def __init__(self, Brand: str, Model: str, Color: str,Speed,SeatCount,ManifactureDate):
        super().__init__(Brand, Model, Color)
        self.Speed=Speed
        self.SeatCount=SeatCount
        self.ManifactureDate=ManifactureDate    
    def getInfo(self):
        s=super().getInfo()+f'''\b\b\b\bSpeed:{self.Speed} \nSeatCount:{self.SeatCount}\nManifactureDate:{self.ManifactureDate}'''
        print(s)
class Truck(Transport):
    def __init__(self, Brand: str, Model: str, Color: str,weightCapacity):
        self.weightCapacity=weightCapacity
        super().__init__(Brand, Model, Color)
        print(super().getInfo()+f"\b\b\b\bYuk kutarish hajmi: {self.weightCapacity} tonna")
t=Transport("BMw","M5","Black")
car=Car("BMW","M5","Black",300,4,2005)
car.getInfo()
truck=Truck("BMW","M5","Black",5)
truck.getInfo()