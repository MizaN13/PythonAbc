class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    pass
class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")

cat1 = Cat()
dog1 = Dog()
cat1.walk()
cat1.be_annoying()
dog1.walk()
