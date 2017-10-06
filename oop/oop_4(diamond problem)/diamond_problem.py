#Diamond problem
class ClassB:
    num_calls_B = 0

    def make_a_cal(self):
        print("calling method in class B")
        self.num_calls_B += 1

class LeftSubClass(ClassB):
    num_left_call = 0

    def make_a_cal(self):
        ClassB.make_a_cal(self)
        print("calling method in leftsubclass")
        self.num_left_call += 1

class RightSubClass(ClassB):
    num_right_call = 0

    def make_a_cal(self):
        ClassB.make_a_cal(self)
        print("calling method in rightclass")
        self.num_right_call += 1

class SubCallA(LeftSubClass, RightSubClass):
    num_call_SubA = 0

    def make_a_cal(self):
        LeftSubClass.make_a_cal(self)
        RightSubClass.make_a_cal(self)
        print("calling method in suba")
        self.num_call_SubA += 1

if __name__ == "__main__":
    s = SubCallA()
    s.make_a_cal()
    print("subClassA: {}".format(s.num_call_SubA))
    print("rightsubclass: {}".format(s.num_right_call))
    print("leftsubclass: {}".format(s.num_left_call))
    print("classB: {}".format(s.num_calls_B))

"""
#output

calling method in class B
calling method in leftsubclass
calling method in class B
calling method in rightclass
calling method in suba
subClassA: 1
rightsubclass: 1
leftsubclass: 1
classB: 2

"""

#from the upperclass we see that the hierrachy(classB) is called twice
#despit that we just called it once in the code