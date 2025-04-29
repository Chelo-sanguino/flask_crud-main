class Articulo:
    def __init__(self, id: int, codigo: str, nombre: str, precio: float = 0.0):
        self._id = id
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio

    def id(self) -> int:
        return self._id

    def codigo(self) -> str:
        return self._codigo

    def nombre(self) -> str:
        return self._nombre

    def precio(self) -> float:
        return self._precio

    def setCodigo(self, value: str) -> None:
        self._codigo = value

    def setNombre(self, value: str) -> None:
        self._nombre = value

    def setPrecio(self, value: float) -> None:
        self._precio = value
