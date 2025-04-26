import os

class exportFile:
    def __init__(self):
        self.ruta = os.getcwd()
    
    def searchDir(self):
        paths = {}
        while True:
            folders = os.listdir()

            fls1 = ('Escritorio', 'Documentos', 'Descargas')
            fls2 = ('Desktop', 'Documents', 'Downloads')

            if fls1[0] in folders:
                ruta = f'{os.getcwd()}\\{fls1[0]}'
                paths.setdefault('desktop', ruta)
            
            if fls1[1] in folders:
                ruta = f'{os.getcwd()}\\{fls1[1]}'
                paths.setdefault('documents', ruta)
            
            if fls1[2] in folders:
                ruta = f'{os.getcwd()}\\{fls1[2]}'
                paths.setdefault('downloads', ruta)
            
            if fls2[0] in folders:
                ruta = f'{os.getcwd()}\\{fls2[0]}'
                paths.setdefault('desktop', ruta)
            
            if fls2[1] in folders:
                ruta = f'{os.getcwd()}\\{fls2[1]}'
                paths.setdefault('documents', ruta)
            
            if fls2[2] in folders:
                ruta = f'{os.getcwd()}\\{fls2[2]}'
                paths.setdefault('downloads', ruta)
            
            if len(paths) == 3:
                break
            else:
                os.chdir('..')
        
        return paths
    
    def newDir(self):
        os.chdir(self.ruta)
        if not os.path.isdir('Nueva carpeta'):
            os.mkdir('Nueva carpeta')
        ruta = os.getcwd()
        return ruta


    def export(self, route:str, data:dict) -> bool:
        """
        Esta funcion permite exportar un archivo con los datos obtenidos
        """
        try:
            with open(route, 'w') as file:
                text = f'GENERO: {data.get("genero")}, DNI: {data.get("dni")}, CUIL: {data.get("cuil")}'
                file.write(text)
            return True
        except Exception as e:
            return False
        
    def getRoute(self, folder:str) -> str:
        if folder == 'newdir':
            new = self.newDir()
            ruta = f'{new}\\Nueva carpeta\\datos.txt'
            return ruta
        else:
            paths = self.searchDir()   
            os.chdir(paths[folder])
            ruta = f'{os.getcwd()}\\datos.txt'
            return ruta