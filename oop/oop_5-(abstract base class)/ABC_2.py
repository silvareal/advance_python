from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    
    @abstractmethod
    def func_1(self):
        pass

    @abstractmethod
    def func_2(self):
        pass

class SubClass(Base):
    def func_1(self):
        pass

print("Trying to generate an Instance for Base Class \n")
a = Base()

'''
output:

Trying to generate an Instance for Base Class

Traceback (most recent call last):
  File "c:/Users/BHADMUS/Desktop/python/advance pthon/oop/oop_5-(abstract base class)/ABC_2.py", line 18
, in <module>
    a = Base()
TypeError: Can't instantiate abstract class Base with abstract methods func_1, func_2

'''