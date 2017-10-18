'''
Thanks to polymophism we can presonalise an a method operator like __add__
'''

class ShoppingCart:

    def __init__(self, product_list):
        self.product_list = product_list

    def __call__(self, product_list= None):
        if product_list is None:
            product_list = self.product_list
        product_list = self.product_list
    
    def __add__(self, other_list):
        added_list = self.product_list

        for p in other_list.product_list.keys():
            if p in self.product_list.keys():
                value = other_list.product_list[p] + self.product_list[p] # it add the value of the given dict
                added_list.update({p: value})
            else:
                added_list.update({ p: other_list.product_list[p] })
        
        return ShoppingCart(added_list)

    def __repr__(self):
        return "\n".join("product {}| Quality {}".format(
            p, self.product_list[p]) for p in self.product_list.keys())
    
if __name__ == "__main__":
    s_cart1 = ShoppingCart({'muffin': 3, 'milk': 2, 'water': 6})
    s_cart2 = ShoppingCart({'milk': 5, 'soda': 2, 'beer': 12})
    s_cart3 = s_cart1 + s_cart2
    print(s_cart3.product_list)
    print(s_cart3)

'''
output:

{'muffin': 3, 'milk': 7, 'water': 6, 'soda': 2, 'beer': 12}
product muffin| Quality 3
product milk| Quality 7
product water| Quality 6
product soda| Quality 2
product beer| Quality 12
'''  