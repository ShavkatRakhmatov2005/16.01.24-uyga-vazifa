class Soldat:
    def __init__(self,name:str,age:int,gender:str,height:float,weight:float):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
class Armiya(Soldat):
    def __init__(self,name,age,gender,height,weight):
        super().__init__(name,age,gender,height,weight)
    def showinfo(self):
        if self.age>18 and self.gender.lower()=='male':
            if self.height<150 and self.weight<75:
                print("Piyoda askar")
            else:
                print("Tank qo'shini")
armiya=[]
for i in range(1, int(input('n='))+1):
    name=input("\nname: ")
    age=int(input('age: '))
    gender=input('gender: ')
    height=float(input('height: '))
    weight=float(input('weight: '))
    soldat=Armiya(name,age,gender,height,weight)
    armiya.append(soldat)
for soldat in armiya:
    soldat.showinfo()