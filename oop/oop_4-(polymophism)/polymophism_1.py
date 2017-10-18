'''
The ability to call a method on a subclass with different behavior is called polymophism
types of polymophism
1.overriding
2.overloading
'''

#overriding example

class Variable:

    def __init__(self, data):
        self.data = data

    def representative(self):
        pass

class Income(Variable):

    def representative(self):
        return sum(self.data) / len(self.data)

class City(Variable):
    
    #class variable
    _city_pop_size = {"lagos":500, "port-harcort":3200,
                "auchi":900, "abujja":2300, "markurdi":700}

    def representative(self):
        dict = {City._city_pop_size[c]:c for c in self.data 
                if c in City._city_pop_size.keys()}
        return dict[max(dict.keys())]

class JobTitle(Variable):
    
    #class variable
    _range = {"CEO":1, "CTO":2, "Analyst":3, "Itern":5}

    def representative(self):
        dict = {JobTitle._range[c]: c for c in self.data
            if c in JobTitle._range.keys()}
        return "min range: " + dict[min(dict.keys())] + "\n" + "keys" + "keys: " + str(dict.keys())

if __name__ == "__main__":
    income_list = Income([50, 60, 70, 80, 90, 20, 10, 20])
    city_list = City(["lagos", "port-harcort",
                "auchi", "abujja", "markurdi"])
    jobtitle = JobTitle(["CEO", "CTO", "Analyst", "Itern"])
    print(income_list.representative())
    print(city_list.representative())
    print(jobtitle.representative())

"""
output:

50.0
port-harcort
min range: CEO
keyskeys: dict_keys([1, 2, 3, 5])

"""