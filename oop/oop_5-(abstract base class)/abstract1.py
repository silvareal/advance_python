'''
abstract classes in programming language allows us to represent abstract object.
Abstract objects are objects creates to be inherited.
it's also a bad idea to instatiate the abstract objects
'''
class Base:

    def func_1(self):
        raise NotImplementedError

    def func_2(self):
        raise NotImplementedError

class SubClass(Base):

    def func_1(self):
        print("func_1 called...")
        return

if __name__ == "__main__":
    b1 = Base()
    b2 = SubClass()
    b2.func_1()
    b2.func_2()

'''
output:

func_1 called...
Traceback (most recent call last):
  File "c:/Users/BHADMUS/Desktop/python/advance pthon/oop/oop_5-(abstract base class)/abstract1.py", lin
e 24, in <module>
    b2.func_2()
  File "c:/Users/BHADMUS/Desktop/python/advance pthon/oop/oop_5-(abstract base class)/abstract1.py", lin
e 12, in func_2
    raise NotImplementedError
NotImplementedError

'''