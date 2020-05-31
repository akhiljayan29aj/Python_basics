## Database handling

#Steps
#1. Connect to database
##import sqlite3 as sq  # import the library
##conn = sq.connect('new.db')  # create the connection variable
##cur = conn.cursor() # create cursor

#2. Execute queries (Operation we perform on database)
##qry='create table if not exists students(id int,name text,marks int)'  # making a query(creating table)
##cur.execute(qry)                 # executing a query
##qry1 = '''insert into students(id,name,marks) values (1,'akhil',80)'''  # (inserting values in table)
##cur.execute(qry1)
##qry2 = '''select * from students where 1'''  # Fetching from the table
##x = cur.execute(qry2)
##print(x.fetchall())

#3. Close the connection
##conn.commit()
##conn.close()


## Classes

class Person:                        # creating a class
    msg = "Welcome to our company"   # defining properties of the class
    def __init__(self, name, age):   # making a constructor
        self.name = name
        self.age = age

    def greet(self):                 # defining a method
        print("Hello my name is", self.name)
        print(Person.msg)
        
class Punjabi:
    msg = "Straight from Chandigarh"
    def __init__(self, name):   
        self.name = name
    def greet(self):                 # method of same name (greet)
        print("Oh ji myself", self.name)
        print(Punjabi.msg)    
    
p1 = Person("Akhil",20) # creating an object with class Person
p2 = Punjabi("Jugdeep")

print(p1.name)
print(p1.age)
p1.greet()    # calling a method on object
p2.greet()    # calling the method with the same name but on diff class


## Polymorphism (used above)
# In Python, Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

## Inheritance

class Block:                     # Parent Class
    def __init__(self,w,l,h):
        self.w = w
        self.l = l
        self.h = h

    def volume(self):
        return self.w*self.l*self.h

    def sayShape(self):
        return "I am a cube"

class ColorBlock(Block):          # Child Class
    def __init__(self,w,l,h,color):
        Block.__init__(self,w,l,h)  # passing the properties of parent to the child when child has some extra properties otherwise not necessary.
        self.color = color

    def sayColor(self):
        return "I am "+self.color+" coloured cube"

class BorderBlock(Block):         # Child Class
    border=1
    def vol(self):
        w= self.w + BorderBlock.border
        h= self.h + BorderBlock.border
        l= self.l + BorderBlock.border
        return w*h*l

block1 = ColorBlock(3,2,2,"red")
block2 = BorderBlock(4,4,4)
print(block1.volume())
print(block1.sayColor())
print(block2.vol())

print(block1.sayShape())
print(block2.volume())















