from sqlalchemy import TIMESTAMP, Column, Enum, Integer, String, Date, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import relationship
from core.db import Base


#Meds user by login 
class MedUser(Base):
    __tablename__ = 'tb_med_users'

    id_med_user = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_medico = Column(Integer, nullable=True)
    st_usuario = Column(String(50), nullable=False)
    st_token = Column(String(99), nullable=False)
    id_rol_usuario = Column(Integer, nullable=True)
    id_activo = Column(Integer, nullable=False)
    dt_fecha_registro = Column(DateTime, nullable=False)
    id_membresia = Column(Integer, nullable=False)


class GeneroEnum(str, Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class EstadoEnum(str, Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Suspendido = "Suspendido"
    Retirado = "Retirado"


    
class MedicosModel(Base):
    __tablename__="tb_medicos"
    
    id_medico = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)

    genero = Column(Enum('Masculino', 'Femenino', 'Otro'), nullable=False)

    id_especialidad = Column(Integer)
    subespecialidad = Column(String(100), nullable=True, default=None)

    numero_licencia = Column(String(50), nullable=False)
    entidad_emisora_licencia = Column(String(100), nullable=False)

    fecha_expedicion_licencia = Column(DateTime, nullable=False)
    fecha_vencimiento_licencia = Column(DateTime, nullable=False)

    cedula_profesional = Column(String(50), nullable=False)
    institucion_formacion = Column(String(150), nullable=False)

    anio_graduacion = Column(Integer, nullable=False)  # Year(4) no existe en SQLAlchemy

    certificaciones_adicionales = Column(Text, nullable=True)

    telefono = Column(String(20), nullable=True, default=None)
    email = Column(String(100), nullable=False, unique=True)

    direccion = Column(Text, nullable=True)
    pais = Column(String(50), nullable=False)
    ciudad = Column(String(100), nullable=False)
    codigo_postal = Column(String(10), nullable=True, default=None)

    fecha_registro = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")

    estado = Column(Enum('Activo', 'Inactivo', 'Suspendido', 'Retirado'), nullable=False, default='Activo')

    motivo_suspension = Column(Text, nullable=True)
    
    foto_perfil_url = Column(String(255), nullable=True, default=None)
    
    id_turno=Column(Integer,nullable=False)


