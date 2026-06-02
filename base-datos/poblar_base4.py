from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import RecursoAcademico, Profesor
import json

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/recursos_academicos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    for d in datos:
        nombres, apellidos = d['profesor'].split(" ", 1)
        profesor = session.query(Profesor).filter_by(nombres=nombres, apellidos=apellidos).first()
        recurso = RecursoAcademico(
            titulo=d['titulo'],
            fecha_publicacion=d['fecha_publicacion'],
            tipo=d['tipo'],
            url=d['url'],
            profesor=profesor
        )
        session.add(recurso)

session.commit()
