import json
class controlador:
    def __init__(self):
        self.objModelo=modelo()
        self.objVista=vista()
        
    def guardar_texto(self):
        texto=self.objVista.tomarTexto()
        texto=self.objModelo.guardarTexto(texto)
        texto=self.objModelo.crearArchivo(texto)
        return texto
    
    def crearArchivo(self,datoTexto):
        nombreArchivo=self.objVista.tomarNombre()
        nombreArchivo=self.objModelo.crearArchivo()
        return nombreArchivo