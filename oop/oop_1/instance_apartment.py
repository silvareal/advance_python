#importing Apertment class from creat_apartment
from create_apartment import Apartment


#assigning value to class instance
flat    = Apartment(_id=1, agent_fee=100, value=500)

print("sold?:", flat.sold) 
flat.sell()  #caling the sell() method
print("sold?:", flat.sold)
flat.sell()    #caling the sell() method

'''
output:

sold?: False
sold?: True
apartment 1 was sold
'''