# Q. Make a fruit class and instantiate different fruits with different arguments.

class Fruit:
    def __init__(self, name, typ, item):   
        self.name = name
        self.typ = typ
        self.item = item
    def isReady(self):                 
        print(self.typ, self.name, self.item, "is ready.")
        
orange = Fruit("Orange","Big","Juice")
apple = Fruit("Apple","Red","Jam")
cucumber = Fruit("Cucumber","Fresh","Salad")

orange.isReady()
apple.isReady()
cucumber.isReady()
