from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import RecursoAcademico, Profesor, Carrera, Facultad

Session = sessionmaker(bind=engine)
session = Session()

facultad_buscada = "Facultad de Ingeniería"

print(f"--- RECURSOS ACADÉMICOS DE LA {facultad_buscada.upper()} ---")

recursos = (
    session.query(RecursoAcademico)
    .join(RecursoAcademico.profesor)
    .join(Profesor.carrera)
    .join(Carrera.facultad)
    .filter(Facultad.nombre_oficial == facultad_buscada)
    .all()
)

for r in recursos:
    print(r)
