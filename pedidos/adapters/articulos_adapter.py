from pedidos.domain.articulos_port import ArticulosPort
from pedidos.domain.articulo import Articulo
from pedidos import *
from pedidos.helpers.pg_command import PGCommand


class ArticulosAdapter(ArticulosPort):

    def __init__(self, db: PGCommand):
        self.db = db

    def get_by_id(self, id: int) -> Articulo | None:
        fila = self.db.queryone(
            """
            select id, codigo, nombre, precio from articulo where id=%(id)s
            """,
            {"id": id},
        )

        if fila is None:
            return None

        return Articulo(fila["id"], fila["codigo"], fila["nombre"], fila["precio"])

    def find_all(self, filtro: str) -> list:
        filas = self.db.queryall(
            """
            select id, codigo, nombre, precio from articulo where nombre LIKE %(filtro)s
            """,
            {"filtro": "%" + filtro + "%"},
        )

        lista = []
        for fila in filas:
            lista.append(Articulo(fila["id"], fila["codigo"], fila["nombre"], fila["precio"]))
        return lista

    def save(self, articulo: Articulo) -> None:
        sql = """
        INSERT INTO articulo (id, codigo, nombre, precio) 
        VALUES (%(id)s, %(codigo)s, %(nombre)s, %(precio)s)
        ON CONFLICT (id) DO UPDATE 
        SET codigo=%(codigo)s, nombre=%(nombre)s, precio=%(precio)s
        """
        self.db.execute(
            sql,
            {
                "id": articulo.id(),
                "codigo": articulo.codigo(),
                "nombre": articulo.nombre(),
                "precio": articulo.precio(),
            },
        )

    def delete(self, articuloId: int) -> None:
        self.db.execute(
            """
            delete from articulo where id=%(id)s
            """,
            {"id": articuloId},
        )

    def get_next_id(self) -> int:
        fila = self.db.queryone(
            """
            select nextval('articulo_id_seq') as id
            """, ()
        )
        return fila["id"]