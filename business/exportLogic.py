class exportFile:
    def __init__(self,dni,genre, cuil):
        self.genre = genre
        self.dni = dni
        self.cuil = cuil
    
    def export(self) -> bool:
        """
        Esta funcion permite exportar un archivo con los datos obtenidos
        """
        try:
            with open('cuil.txt', 'w') as file:
                text = f'GENERO: {self.genre}, DNI: {self.dni}, CUIL: {self.cuil}'
                file.write(text)
            return True
        except Exception as e:
            return False
        
        