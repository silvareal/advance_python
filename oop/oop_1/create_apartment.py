"""we name classes using CAMELCASE and we name methods using SNAKECASE"""

#creating a class apartment representing an apartment for sale in USD
class Apartment:

    #instantiating the class with the __init__ method
    def __init__(self, _id, agent_fee, value):
        self._id        = _id
        self.agent_fee  = agent_fee
        self.value      = value
        self.sold       = False
    
    def sell(self):
        if not self.sold:
            self.sold  = True
        else:
            print(
                "apartment {} was sold"
                .format(self._id))

                