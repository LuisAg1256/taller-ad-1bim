from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Carrera, Facultad
import json

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/carreras.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    for d in datos:
        facultad = session.query(Facultad).filter_by(nombre_oficial=d['facultad']).first()
        carrera = Carrera(
            nombre=d['nombre'],
            codigo=d['codigo'],
            facultad=facultad
        )
        session.add(carrera)

session.commit()
