#it generates an error because it cannot create a consistennt logical order

class x():
    def call_me(self):
        print("i ma x")

class y():
    def call_me(self):
        print("i am y")

class a(x,y):
    def call_me(self):
        print("i am a")

class b(y,x):
    def call_me(self):
        print("i am b")

class f(a,b):
    def call_me(self):
        print("i am f")        

#TypeError: Cannot create a consistent method resolution
#order (MRO) for bases x, y

'''
output:
Traceback (most recent call last):
  File "invalid_structure.py", line 18, in <module>
    class f(a,b):
TypeError: Cannot create a consistent method resolution
order (MRO) for bases x, y

'''