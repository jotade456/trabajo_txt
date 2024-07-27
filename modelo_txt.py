import json
class archivo:
    def __init__(self):
        self.archivo = None

    def get_archivo(self):
        return self.archivo
    
    def set_archivo(self,datoArchivo):
        self.archivo = datoArchivo
        return self.archivo

    def guardarTexto(self,datoTexto):
        auxtexto=datoTexto
        return auxtexto
    
    def crearArchivo(self,datoNombre,datoAux_texto):
        nombreArchivo=datoNombre
        nombreArchivo=nombreArchivo+".txt"
        with open(nombreArchivo,"w") as archivoTexto:
            #escriba una cadena de texto en su archivo
            archivoTexto.write(datoAux_texto)
            archivoTexto.close()

    def descerializar(self,datoArchivo):
        objDescerializar=json.loads(datoArchivo)
        print("Longitud: ",len(datoArchivo))
        return objDescerializar
