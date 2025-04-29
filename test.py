import sqlite3


def dict_factory(cursor, row):
    if row is None:
        return None
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


con = sqlite3.connect("/home/ronal/PycharmProjects/columnas/application/data/database.db")
con.row_factory = dict_factory
cursor = con.cursor()


data = cursor.execute(
            "SELECT * FROM project WHERE id = ?",
            ('454c7228-6e43-4083-9516-43e5d7e761a5',),
        ).fetchone()
print(type(data))
print(data)
# print("Ejecutando.............")
# r = cursor.execute("INSERT INTO project (id, name) VALUES('ssssss', 'nnnnnnn')")
# print(r)
# con.commit()

print("Imprimiendo.............")
data = cursor.execute(
            "SELECT * FROM prueba"
        ).fetchall()
print(type(data))
print(data)