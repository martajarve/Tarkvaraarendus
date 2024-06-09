class Pause(object):
    def __init__(self, paused=False):
        # Pause klassi konstruktor
        self.paused = paused  # Kas mäng on peatatud
        self.timer = 0  # Ajatimer
        self.pauseTime = None  # Aeg, mille jooksul mäng on peatatud
        self.func = None  # Funktsioon, mis käivitatakse pärast pausi

    def update(self, dt):
        # Uuendab pausi olekut ja tagastab funktsiooni, kui aeg on möödas
        if self.pauseTime is not None:
            self.timer += dt
            if self.timer >= self.pauseTime:
                self.timer = 0
                self.paused = False  # Paugistaatust muudetakse
                self.pauseTime = None
                return self.func  # Tagastab funktsiooni, mida tuleb käivitada pärast pausi
        return None

    def setPause(self, playerPaused=False, pauseTime=None, func=None):
        # Seab pausi atribuudid ja käivitab pausi
        self.timer = 0
        self.func = func  # Määra funktsioon, mis käivitatakse pärast pausi
        self.pauseTime = pauseTime  # Määra pausi aeg
        self.flip()  # Muuda pausi olekut

    def flip(self):
        # Muudab pausi olekut
        self.paused = not self.paused
