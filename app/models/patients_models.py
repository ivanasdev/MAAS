from sqlalchemy import TIMESTAMP, Column, Enum, Integer, String, Date, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import relationship
from core.db import Base

class Paciente(Base):  
    __tablename__ = "tb_pacientes"

    paciente_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero_id = Column(Integer, nullable=False)
    direccion = Column(Text, nullable=True)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    fecha_registro = Column(DateTime, nullable=False, default=func.now())
    historial_medico_id = Column(Integer,  nullable=True)
    alergias_id = Column(Integer, nullable=True)
    antecedentes_familiares_id = Column(Integer, nullable=True)
    historial_farmacos_id = Column(Integer,  nullable=True)
    estado_id = Column(Integer, nullable=True)

