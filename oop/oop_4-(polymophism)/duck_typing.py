'''
The most common way to deﬁne it is "If it walks like a duck and quacks like a duck,then it is a duck."
'''

class Duck:

    def scream(self):
        print("Quack")
    
    def walk(self):
        print("walking like a duck...")

class Person:

    def scream(self):
        print("ahahaha")
    
    def walk(self):
        print("walking like a human...")


def activate(duck):
    duck.scream()
    duck.walk()

if __name__ == "__main__":
    Donald = Duck()
    John = Person()
    activate(Donald)
    activate(John)

'''
output:

Quack
walking like a duck...
ahahaha
walking like a human...
'''