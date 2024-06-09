import math # Impordib math mooduli.

class Vector2(object): # Määratleb Vector2 klassi.
    def __init__(self, x=0, y=0): # Konstruktor, mis initsialiseerib Vector2 objekti.
        self.x = x # Määrab x-koordinaadi.
        self.y = y # Määrab y-koordinaadi.
        self.thresh = 0.000001 # Määrab künnise.

    def __add__(self, other): # Operaator "+" ülelaadimine.
        return Vector2(self.x + other.x, self.y + other.y) # Tagastab uue Vector2 objekti, mis on kahe vektori summa.

    def __sub__(self, other): # Operaator "-" ülelaadimine.
        return Vector2(self.x - other.x, self.y - other.y) # Tagastab uue Vector2 objekti, mis on kahe vektori vahe.

    def __neg__(self): # Operaatori "-" ülelaadimine (negatsioon).
        return Vector2(-self.x, -self.y) # Tagastab uue Vector2 objekti, mille koordinaadid on vastandväärtustega.

    def __mul__(self, scalar): # Operaator "*" ülelaadimine (skalaariga korrutamine).
        return Vector2(self.x * scalar, self.y * scalar) # Tagastab uue Vector2 objekti, mille koordinaadid on korrutatud skalaariga.

    def __div__(self, scalar): # Operaator "/" ülelaadimine (skalaariga jagamine).
        if scalar != 0: # Kontrollib, kas skalaar ei ole null.
            return Vector2(self.x / float(scalar), self.y / float(scalar)) # Tagastab uue Vector2 objekti, mille koordinaadid on jagatud skalaariga.
        return None # Tagastab None, kui skalaar on null.

    def __truediv__(self, scalar): # Operaatori "//" ülelaadimine (täisarvude jagamine).
        return self.__div__(scalar) # Kasutab skalaariga jagamise operaatorit.

    def __eq__(self, other): # Operaator "==" ülelaadimine (võrdlemine).
        if abs(self.x - other.x) < self.thresh: # Kontrollib x-koordinaatide lähedust.
            if abs(self.y - other.y) < self.thresh: # Kontrollib y-koordinaatide lähedust.
                return True # Tagastab True, kui mõlema koordinaadi vahe on väiksem kui künnis.
        return False # Tagastab False, kui vahe on suurem kui künnis.

    def magnitudeSquared(self): # Arvutab vektori pikkuse ruudu.
        return self.x**2 + self.y**2 # Tagastab vektori pikkuse ruudu.

    def magnitude(self): # Arvutab vektori pikkuse.
        return math.sqrt(self.magnitudeSquared()) # Tagastab vektori pikkuse.

    def copy(self): # Loob vektori koopia.
        return Vector2(self.x, self.y) # Tagastab uue Vector2 objekti, mis on antud vektori koopia.

    def asTuple(self): # Tagastab vektori tuple kujul.
        return self.x, self.y # Tagastab tuple koordinaatidena.

    def asInt(self): # Tagastab vektori täisarvulistena.
        return int(self.x), int(self.y) # Tagastab täisarvulistena koordinaadid.

    def __str__(self): # Operaator "__str__" ülelaadimine (stringi esitamine).
        return "<"+str(self.x)+", "+str(self.y)+">" # Tagastab vektori esituse stringina "<x, y>".
