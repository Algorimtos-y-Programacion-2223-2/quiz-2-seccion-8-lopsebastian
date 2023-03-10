class Edificio(): 
    def __init__(self, nombre, pisos, calle, ciudad, cod, apartamentos):
        self.nombre = nombre
        self.pisos = pisos
        self.calle = calle
        self.ciudad = ciudad
        self.cod = cod
        self.apartamentos = apartamentos
        self.lista = [] 

    def construir(self): 
        nombre = input("Nombre del edificio: ")
        pisos = input("Pisos: ")
        while not pisos.isnumeric: 
            pisos = input("Numero de pisos: ")
        calle = input("Calle: ")
        ciudad = input("Ciudad: ")
        cod = input("Codigo postal: ")
        while not cod.isnumeric(): 
            cod = input("Codigo postal: ")
        apartamentos = input("Apartamentos: ")
        while not apartamentos.isnumeric(): 
            apartamentos = input("numero de apartamentos: ")
        Edificio(nombre, pisos, calle, ciudad, cod, apartamentos)
        self.lista.append(Edificio)


    def mostrar_direccion(self): 
        print(f"""
        Nombre: {self.nombre}
        Pisos: {self.pisos}
        Calle: {self.calle}
        Ciudad: {self.ciudad}
        """)
    
    def clasificacion_edificio(self):
        if self.apartamentos > (self.pisos * 4): 
            tipo = "Bloque Residencial"
            print(f"El edificio es de tipo {tipo}")
        else:
            tipo = "Edificio Residencial"
            print(f"El edificio es de tipo {tipo}")

    def mostrar_apartamentos(self): 
        for edificio in self.lista: 
            print(edificio)
        

