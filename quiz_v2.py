class Dog:
    def __init__(self, name):
        self.name = name

    def Bark(self):
        print(self.name + " says Woof!")


my_Dog = Dog("Max")
print(my_Dog.name)

rex = Dog("Rex")
buddy = Dog("Buddy")
rex.Bark()
buddy.Bark()