#calling a superclasss' __init__ into the customer class is highly
#not recommended,reference to the previous topic diamond problem

class AddressHolder:
    def __init__(self, street, number, city, state):
        self.street = street
        self.number = number
        self.city   = city
        self.state  = state

class Contact:
    contact_list = []
    
    def __init__(self, name, email):
        self.name = name
        self.email =email
        Contact.contact_list.append(self)

class Customer(AddressHolder, Contact):
    
    def __init__(self,street, number,city, state, name, email, phone):
        AddressHolder.__init__(self)
        Contact.__init__(self)
        self.phone = phone

