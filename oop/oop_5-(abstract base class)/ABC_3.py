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
    
    def func_2(self):
        pass

print("SubClass: {}".format(issubclass(SubClass, Base)))
print("instance: {}".format(isinstance(SubClass(), Base)))

'''
output:

SubClass: True
instance: True
'''