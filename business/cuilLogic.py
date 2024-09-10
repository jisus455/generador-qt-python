
class cuilCalculator:
    def __init__(self,dni,genre):
        self.dni = dni
        self.genre = genre
        self.genredigits="00"

    def validate(self):
        try:
            self.dni = int(self.dni)
            self.dni = abs(self.dni) #esto es para evitar errores si es negativo
        except ValueError:
            raise Exception('El dni deben ser solo numeros')
        self.dni = str(self.dni)
        long = len(self.dni)
        if long > 8:
            raise Exception("El dni debe tener maximo 8 digitos")
        else:
            cant_ceros = 8-long
            while cant_ceros > 0:
                self.dni = "0" + self.dni
                cant_ceros = cant_ceros - 1

    def calculate(self):

        if self.genre.upper() == "M":
            self.digitsgenre = "20"
        if self.genre.upper() == "F":
            self.digitsgenre = "27"
        
        partial = self.digitsgenre + self.dni
        constants = (5,4,3,2,7,6,5,4,3,2)
        i = 0
        res = 0
        for digit in partial:
            res = res + constants[i]*int(digit)
            i = i+1

        verifDigit = res%11
        if verifDigit > 1:
            verifDigit = 11-verifDigit
        if verifDigit == 1:
            self.digitsgenre = "23"
            if self.genre.upper() == "M":
                verifDigit = 9
            if self.genre.upper() == "F":
                verifDigit = 4
        return self.digitsgenre + "-" + self.dni + "-" + str(verifDigit)

