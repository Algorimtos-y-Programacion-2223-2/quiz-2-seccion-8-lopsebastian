from Productos import Productos
from Hogar import Hogar
from Ropa import Ropa
from Gaming import Gaming


class App(): 
    products = [
    { "id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800 },
    { "id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600 },
    { "id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25 },
    { "id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5 },
    { "id": 5, "name": "Laptop Gamer", "type": "Gaming", "stock": 11, "price": 2500 },
    { "id": 6, "name": "Nintendo Switch OLED", "type": "Gaming", "stock": 25, "price": 400 },
    ]

    products_act = []
    

    def guardar_productos(self): 
        for element in self.products: 
            for producto in element.items(): 
                self.products_act.append(producto)
                return self.products_act

    def agregar_producto(self): 
        name = input("Nombre del producto: ")
        stock = input("Stock: ")
        while not stock.isnumeric(): 
            stock = input("por favor ingrese la cantidad de stock: ")
        price = input("Precio del producto: ")
        while not price.isnumeric(): 
            price = input("Por favor ingrese el precio: ")
        tipo = input("""
        1. Hogar
        2. Ropa
        3. Gaming
        """)
        while not tipo.isnumeric() or int(tipo) not in range(1, 4): 
            tipo = input("Por favor ingrese un caracter valido: ")

        if tipo == "1": 
            type = "Hogar"
            p = Hogar(name, type, stock, price)
            self.products_act.append(p)
        elif tipo == "2": 
            type = "Ropa"
            p = Ropa(name, type, stock, price)
            self.products_act.append(p)
        elif tipo == "3": 
            type = "Gaming"
            p = Gaming(name, type, stock, price)
            self.products_act.append(p)
            print(self.products_act)
        return self.products_act


    def ver_productos(self): 
        print("VER PROUDUCTOS")
        for element in self.products_act: 
            print(f"""
            Nombre = {element["name"]}
            Tipo = {element["type"]}
            Stock = {element["stock"]}
            Precio = {element["price"]}
            """)

    def start(self):
        self.guardar_productos()
        print("""
        MENU PRINCIPAL
        1. Agregar producto
        2. Ver producto
        3. Salir
        """)
        option = input("Ingrese una opcion: ")
        while not option.isnumeric() or int(option) not in range(1, 4): 
            option = input("Por favor inrese una opcion correcta")
        
        if option == "1": 
            self.agregar_producto()
            self.start()

        elif option == "2": 
            self.ver_productos()
            self.start()

        else: 
            print("Fin del programa")