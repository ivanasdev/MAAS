from datetime import date
from typing import Optional
from pydantic import BaseModel

class PacienteFiltroRequest(BaseModel):
    paciente_id: Optional[int] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    genero_id: Optional[int] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    fecha_registro: Optional[date] = None
    historial_medico_id: Optional[int] = None
    alergias_id: Optional[int] = None
    antecedentes_familiares_id: Optional[int] = None
    historial_farmacos_id: Optional[int] = None
    estado_id: Optional[int] = None


class PacienteCreate(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    genero_id: int
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    historial_medico_id: Optional[int] = None
    alergias_id: Optional[int] = None
    antecedentes_familiares_id: Optional[int] = None
    historial_farmacos_id: Optional[int] = None
    estado_id: Optional[int] = None