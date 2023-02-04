class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    def description(self):
        print(f"name is : {self.name} \n age is : {self.age} ")
    def get_info(self):
        print(f"coat color is: {self.coat_color}")
        
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def is_hyper(self):
        print(f"{self.name} is a hyper Jack Russell Terrier!")
        
    def is_small(self):
        print(f"{self.name} is a small dog.")
        
        
class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def is_strong(self):
        print(f"{self.name} is a strong Bulldog.")     
    def is_loyal(self):
        print(f"{self.name} is a loyal Bulldog.")
dog1=JackRussellTerrier("max",5,"brown and white")
dog1.description()
dog1.get_info()
dog1.is_hyper()
dog1.is_small()

dog2=Bulldog("buddy",8,"brindle")
dog2.description()
dog2.get_info()
dog2.is_strong()
dog2.is_loyal()
