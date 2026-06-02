from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad

Session = sessionmaker(bind=engine)
session = Session()

print("--- TODAS LAS FACULTADES (Usando all()) ---")
facultades = session.query(Facultad).all()
for f in facultades:
    print(f)
