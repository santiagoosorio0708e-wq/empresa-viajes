class AgenciaException(Exception):
    """Excepción base para la aplicación."""
    pass

class ElementoNoEncontradoError(AgenciaException):
    """Lanzada cuando no se encuentra un elemento en la base de datos."""
    pass

class ValidacionError(AgenciaException):
    """Lanzada cuando un dato de entrada es inválido."""
    pass
