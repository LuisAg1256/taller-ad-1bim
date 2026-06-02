from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Profesor, Carrera
import json

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/profesores.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    for d in datos:
        carrera = session.query(Carrera).filter_by(nombre=d['carrera']).first()
        profesor = Profesor(
            nombres=d['nombres'],
            apellidos=d['apellidos'],
            correo=d['correo'],
            especialidad=d['especialidad'],
            carrera=carrera
        )
        session.add(profesor)

session.commit()
