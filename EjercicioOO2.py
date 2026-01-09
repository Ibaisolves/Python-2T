class Jugador:
    # Constructor
    def __init__(self, dor, nom, eq):
        self.dorsal = dor
        self.nombre = nom
        self.equipo = eq
    
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre} - {self.equipo.nombre_equipo}")

class Equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq


# Programa Principal

Equipo1 = Equipo("Al Nassr")
Equipo2 = Equipo("Real Madrid")
Equipo3 = Equipo("Perilleta FC")

Jugador1 = Jugador(7,"Cristiano Ronaldo",Equipo2)
Jugador2 = Jugador(10,"Kylian Mbappé",Equipo2)
Jugador3 = Jugador(12,"Marcelo",Equipo2)


Jugador1.mostrar()
Jugador2.mostrar()
Jugador3.mostrar()