class Jugador:
    # Constructor
    def __init__(self, dor, nom):
        self.dorsal = dor
        self.nombre = nom
    
    def mostrar(self):
        print(f"{self.dorsal}.{self.nombre}")

# Programa Principal
Jugador1 = Jugador(7,"Cristiano Ronaldo")
Jugador2 = Jugador(10,"Kylian Mbappé")
Jugador3 = Jugador(7,"O Rey")

Jugador1.mostrar()
Jugador2.mostrar()
Jugador3.mostrar()
