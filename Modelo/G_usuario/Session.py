from .Administrador import Administrador

class Session:
    _instance = None

    '''
    Metodo que crea una instancia de la clase Session si no existe una ya creada.
    En caso de que ya exista una instancia, regresa la instancia ya creada.
    '''
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Inicialización de la sesión
        return cls._instance

    def __init__(self):
        self.usuario_autenticado = None

    def iniciar_sesion(self, usuario):
        self.usuario_autenticado = usuario

    def cerrar_sesion(self):
        self.usuario_autenticado = None

    def obtener_usuario_autenticado(self):
        return self.usuario_autenticado

    def esta_autenticado(self):
        return self.usuario_autenticado is not None

    def es_administrador(self):
        # Supongamos que Administrador es una clase existente para usuarios administradores
        return isinstance(self.usuario_autenticado, Administrador)
