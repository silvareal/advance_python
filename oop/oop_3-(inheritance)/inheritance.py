
class GloceryList(list):
    
    def discard(self, price):
        for product in self:
            if product.price > price:
                #remove is in list class
                self.remove(product)
        return self

    def __str__(self):
        out = "The GloceryList\n\n"
        for p in self:
            out += "name: " + p.name + " -price: " + str(p.price) + "\n"
        return out

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == "__main__":
    glocery_list = GloceryList()
    glocery_list.extend([Product("silva",10),Product("akubo",8),Product("ojoshegbe",12)])
    print(glocery_list)
    glocery_list.discard(11)
    print(glocery_list)