'''
onlike other programming language python, does not have an inbuild way to declare Abstract class
but fortunately it has the ABC(Abstarct Base Class)
'''

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

print("is it a subclass: {}".format(issubclass(SubClass, Base)))
print("is a instance: {}".format(issubclass(SubClass(), Base)))

'''
output:

is it a subclass: True
Traceback (most recent call last):
  File "c:/Users/BHADMUS/Desktop/python/advance pthon/oop/oop_5-(abstract base class)/ABC.py", line 23,
in <module>
    print("is a instance {} :".format(issubclass(SubClass(), Base)))
TypeError: Can't instantiate abstract class SubClass with abstract methods func_2

'''