from Productos import Productos

class Ropa(Productos): 

    def __init__(self, name, type, stock, price): 
        super().__init__(name, type, stock, price)

    

    def show(self): 
        print(f" Nombre: {self.name}, Tipo = {self.type}, Stock = {self.stock}, Precio = {self.price}")