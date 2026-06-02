from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from configuracion import engine
from crear_base_entidades import RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

print("--- RECURSOS QUE SON LIBROS O VIDEOS (Usando or_()) ---")
recursos = session.query(RecursoAcademico).filter(or_(RecursoAcademico.tipo == "Libro", RecursoAcademico.tipo == "Video")).all()
for r in recursos:
    print(r)
