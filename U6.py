class Cars:
    def __init__(self,id:int,first_name:str,last_name:str,gender:str,brand:str,year:int,color:str,country:str):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.brand=brand
        self.year=year
        self.color=color
        self.country=country
    def findMaxBrand(self):
        dct={}
        for car in cars:
            dct[car.brand]=dct.get(car.brand,0)+1
        my_brand = max(dct, key=lambda x: dct[x])
        print(f"Brandi eng ko'p avtomabil:{my_brand}")
    def shortCar(self):
        for car in cars:
            if car.year<2005:
                print(f'''
Hurmatli {first_name} {last_name}!
{brand} tomonidan {year} yilda da ishlab chiqarilgan {color} rangli avtoulovingiz 
Texnik holatini tekshirish maqsadida Mahalliy 'Avtotest Corp' ofisiga murojat qilishingizni so'raymiz!
''')
    def shortCar(self):
        if self.year<2005:
            print(f'''
Hurmatli {self.first_name} {self.last_name}!
{self.brand} tomonidan {self.year} yilda da ishlab chiqarilgan {self.color} rangli avtoulovingiz 
Texnik holatini tekshirish maqsadida Mahalliy 'Avtotest Corp' ofisiga murojat qilishingizni so'raymiz!
''')
cars=[]
for i in range(1,int(input('n='))+1):
    id=int(input('ID: '))
    first_name=input('First name: ')
    last_name=input('Last name: ')
    gender=input('Gen: ')
    brand=input("Brand: ")
    year=int(input('Year: '))
    color=input("Color: ")
    country=input('Country: ')
    car=Cars(id,first_name,last_name,gender,brand,year,color,country)
    cars.append(car)
count=0
count1=0

for car in cars:  
    if car.gender.lower()=='male':
        count+=1
    elif car.gender.lower()=='female':
        count1+=1 
if count>count1:
    print(f"Erkaklar Ayollarga nisbatan {count//count1*100} marta ko'proq ")
elif count==count1:
    print("Erkaklar va Ayollar teng nisbatli")
else:
    print(f"Ayollar Erkaklarga nisbatan {count1//count*100} marta ko'proq ")
car.shortCar()
car.findMaxBrand()