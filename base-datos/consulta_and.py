from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from configuracion import engine
from crear_base_entidades import Profesor

Session = sessionmaker(bind=engine)
session = Session()

print("--- PROFESOR LLAMADO 'Ana' Y APELLIDO 'Romero' (Usando and_()) ---")
profesores = session.query(Profesor).filter(and_(Profesor.nombres == "Ana", Profesor.apellidos == "Romero")).all()
for p in profesores:
    print(p)
