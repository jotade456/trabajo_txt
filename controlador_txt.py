from vistaa import Vista
from modelo_txt import archivo
class controlador:
    def __init__(self):
        self.objModelo=archivo()
        self.objVista=Vista(self)
        
    def guardarDatos(self,datoTexto,nombreArchivo):
        texto=self.objModelo.guardarTexto(datoTexto)
        nombreArchivo=self.objModelo.crearArchivo(texto,nombreArchivo)
        return nombreArchivo
        
    def deserializar (self,nombreArchivo):
        texto=self.objModelo.deserializar(nombreArchivo)
        return texto
    
    def ejecutar(self):
        self.objVista.iniciar()
        
objEjecutar=controlador()
objEjecutar.ejecutar()