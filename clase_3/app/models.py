from sqlalchemy import Column, Integer, String

from app.database import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)


class Alumno(Base):
    __tablename__ = "alumno"
    id = Column(Integer, primary_key=True, index=True)
    carrera = Column(String, nullable=True)
