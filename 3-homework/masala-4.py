class Car:
    def __init__(self,name,color,made_year):
        self.name = name
        self.color = color
        self.made_year = made_year

class Nexia_2(Car):
    def nexia_info(self):
        return f"mashina nomi: {self.name}, mashina rangi: {self.color}, ishlab chiqarilgan yili: {self.made_year}"


class Gentra(Car):
    def gentra_info(self):
        return f"mashina nomi: {self.name}, mashina rangi: {self.color}, ishlab chiqarilgan yili: {self.made_year} " 
    
class Cobalt(Car):
    def cobalt_info(self):
        return f"mashina nomi: {self.name}, mashina rangi: {self.color}, ishlab chiqarilgan yili: {self.made_year} " 
    

print("birinchhi mashina")
mashina1 = Nexia_2("nexia 2", "oq", 2016)
print(mashina1.nexia_info())

print("ikkinchi mashina")
mashina2 = Gentra("gentra", "oq", 2023)
print(mashina2.gentra_info())

print("uchinchi mashina")
mashina3 = Cobalt("cobalt", "dark blue", 2024)
print(mashina3.cobalt_info())