class Dog:

    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_into(self):
        print(f"{self.name} has a {self.coat_color} coat.")

class JackRussellTerrier(Dog):

    def happy(self):
        print(f"{self.name} is a Jack Russell and lives very happily.")

    def energetic(self):
        print(f"{self.name} is energetic dog with a strong desire to work.")

class Bulldog(Dog):

    def sensitive(self):
        print(f"{self.name} is a Bull Dog and they are sensitive to cold weather.")
    
    def hot(self):
        print(f"My {self.name} can't tolerate heat and humidity.")


jack = JackRussellTerrier("Hancock","1 yr","white and brown")
jack.description()
jack.get_into()
jack.happy()
jack.energetic()

bullbog = Bulldog("Jimmy","2 yr","Brown")
bullbog.description()
bullbog.get_into()
bullbog.sensitive()
bullbog.hot()

