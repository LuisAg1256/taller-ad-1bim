from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import engine

Base = declarative_base()

class Facultad(Base):
    __tablename__ = 'facultad'
    id = Column(Integer, primary_key=True)
    nombre_oficial = Column(String(100), nullable=False)
    ubicacion = Column(String(100), nullable=False)
    decano = Column(String(100), nullable=False)

    carreras = relationship("Carrera", back_populates="facultad")

    def __str__(self):
        return f"Facultad[ID={self.id}, Nombre='{self.nombre_oficial}', Ubicación='{self.ubicacion}', Decano='{self.decano}']"


class Carrera(Base):
    __tablename__ = 'carrera'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(50), nullable=False)
    facultad_id = Column(Integer, ForeignKey('facultad.id'))

    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

    def __str__(self):
        return f"Carrera[ID={self.id}, Nombre='{self.nombre}', Código='{self.codigo}', ID_Facultad={self.facultad_id}]"


class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    carrera_id = Column(Integer, ForeignKey('carrera.id'))

    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __str__(self):
        return f"Profesor[ID={self.id}, Nombres='{self.nombres}', Apellidos='{self.apellidos}', Correo='{self.correo}', Especialidad='{self.especialidad}', ID_Carrera={self.carrera_id}]"


class RecursoAcademico(Base):
    __tablename__ = 'recurso_academico'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(String(50), nullable=False)
    tipo = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesor.id'))

    profesor = relationship("Profesor", back_populates="recursos")

    def __str__(self):
        return f"RecursoAcademico[ID={self.id}, Título='{self.titulo}', Fecha='{self.fecha_publicacion}', Tipo='{self.tipo}', URL='{self.url}', ID_Profesor={self.profesor_id}]"


Base.metadata.create_all(engine)
