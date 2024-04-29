import os

class State:
    def scan(self):
        pass  

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def scan(self):
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def scan(self):
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate
    
    def toggle_M(self):
        print("Cambiando a Radios Memorizadas")
        self.radio.state = self.radio.rm

class RadiosMemorizadas(State):
    def __init__(self, radio):
        self.radio = radio
        self.fmstate = FmState(radio)
        self.amstate = AmState(radio)
        self.name = "Memorized"
        self.stations = []
        self.pos = 0
        self.init_memorized_stations()

    def init_memorized_stations(self):
        self.M1 = self.fmstate.stations[1] + " M1"
        self.M2 = self.amstate.stations[1] + " M2"
        self.M3 = self.fmstate.stations[2] + " M3"
        self.M4 = self.amstate.stations[0] + " M4"
        self.stations = [self.M1, self.M2, self.M3, self.M4]

    def scan(self):
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.rm = RadiosMemorizadas(self)
        self.state = self.amstate  

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def toggle_M(self):
        if isinstance(self.state, FmState):
            self.state.toggle_M()
        else:
            print("No se puede cambiar a Radios Memorizadas en el estado actual")

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2 + [radio.toggle_M] + [radio.scan] * 4

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
