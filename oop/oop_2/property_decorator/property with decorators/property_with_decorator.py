#property with decorator

def Color:

    def __init__(self, rgb_code, name):
        self.rgb_code  = rgb_code
        self._name     = name'

    #create a property using name of attribute. then we
    #define how to get/set/delete it

    @property
    def name(self):
        print("function to get the color")
        return self._name

    @name.setter
    def name(self, new_name):
        print("function to get the name as {}".format(self.new_name))
        self._name = new_name

    @name.deleter
    def name(self):
        print("erasing color...")
        del sel._name