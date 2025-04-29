
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class MedUserSchema(BaseModel):
    id_medico:int
    st_usuario:str
    st_token:str
    id_rol_usuario:int
    id_activo:int
    dt_fecha_registro: datetime
    id_membresia:int
    class Config:
        orm_mode = True



class MedicoLoginRequest(BaseModel):
    st_usuario: str
    st_token: str

    class Config:
        orm_mode = True



class GeneroEnum(str, Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class EstadoEnum(str, Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Suspendido = "Suspendido"
    Retirado = "Retirado"

class MedicoCreate(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: datetime
    genero: GeneroEnum
    id_especialidad: int
    subespecialidad: Optional[str] = None
    numero_licencia: str
    entidad_emisora_licencia: str
    fecha_expedicion_licencia: datetime
    fecha_vencimiento_licencia: datetime
    cedula_profesional: str
    institucion_formacion: str
    anio_graduacion: int
    certificaciones_adicionales: Optional[str] = None
    telefono: Optional[str] = None
    email: str
    direccion: Optional[str] = None
    pais: str
    ciudad: str
    codigo_postal: Optional[str] = None
    estado: EstadoEnum = EstadoEnum.Activo
    motivo_suspension: Optional[str] = None
    foto_perfil_url: Optional[str] = None

