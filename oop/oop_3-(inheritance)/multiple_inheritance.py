
class Researcher:

    def __init__(self, field):
        self.field = field
    
    def __str__(self):
        out = "The researcher field: " + self.field + "\n"
        return out

class Teacher:

    def __init__(self, courses_list):
        self.courses_list = courses_list

    def __str__(self):
        out = "Teachers courses:"
        for p in self.courses_list:
            out += p + ","
        #out[:-2] selct all the element
        # except the last two 
        return out[:-2] + "\n"

class Profession(Teacher, Researcher):
    
    def __init__(self, name, field, courses_list):
        #these is not completely right
        #soon we will see why in -->oop4(diamond problem)
        Teacher.__init__(self, courses_list)
        Researcher.__init__(self, field)
        self.name = name
    
    def __str__(self):
        out = Teacher.__str__(self)
        out += Researcher.__str__(self)
        out += "name:" + self.name
        return out

if __name__ == '__main__':
    p = Profession("silva",
        "programming",
        ["algorithm","maths","computer","physics"])
    print(p)
        
