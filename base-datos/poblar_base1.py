from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad
import json

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/facultades.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    for d in datos:
        facultad = Facultad(
            nombre_oficial=d['nombre'],
            ubicacion=d['ubicacion'],
            decano=d['decano']
        )
        session.add(facultad)

session.commit()
