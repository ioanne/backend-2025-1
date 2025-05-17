from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from .database import Base # Esto es una importacion relativa
from api.core.database import Base # Esto es una importación absoluta


class Ejemplo(Base):
    __tablename__ = "ejemplo"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=True)
