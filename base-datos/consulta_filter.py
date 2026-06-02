from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Profesor

Session = sessionmaker(bind=engine)
session = Session()

print("--- PROFESORES CON ESPECIALIDAD 'Bases de Datos' (Usando filter()) ---")
profesores = session.query(Profesor).filter(Profesor.especialidad == "Bases de Datos").all()
for p in profesores:
    print(p)
