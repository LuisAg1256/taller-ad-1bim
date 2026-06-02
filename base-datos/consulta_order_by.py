from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Carrera

Session = sessionmaker(bind=engine)
session = Session()

print("--- CARRERAS ORDENADAS ALFABÉTICAMENTE (Usando order_by()) ---")
carreras = session.query(Carrera).order_by(Carrera.nombre).all()
for c in carreras:
    print(c)
