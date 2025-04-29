from datetime import datetime
from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
#Models
from models.meds_model import MedUser,MedicosModel
#Schemas 
from schemas.meds_schema import MedUserSchema,MedicoCreate
from schemas.pacientes_schema import PacienteFiltroRequest,PacienteCreate
from models.patients_models import Paciente


#Login medicos 
async def get_users_auth(request, db: AsyncSession):

    stmt = select(MedUser).where(MedUser.st_usuario == request.st_usuario)
    result = await db.execute(stmt)
    med_user = result.scalars().first()

    
    if not med_user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    return med_user

#Registrar Medico
async def crear_medico(data: MedicoCreate, db: AsyncSession):
    nuevo_medico = MedicosModel(
        nombre=data.nombre,
        apellido=data.apellido,
        fecha_nacimiento=data.fecha_nacimiento,
        genero=data.genero.value,  # OJO: Si estás usando Enum de Pydantic, usa .value
        id_especialidad=data.id_especialidad,
        subespecialidad=data.subespecialidad,
        numero_licencia=data.numero_licencia,
        entidad_emisora_licencia=data.entidad_emisora_licencia,
        fecha_expedicion_licencia=data.fecha_expedicion_licencia,
        fecha_vencimiento_licencia=data.fecha_vencimiento_licencia,
        cedula_profesional=data.cedula_profesional,
        institucion_formacion=data.institucion_formacion,
        anio_graduacion=data.anio_graduacion,
        certificaciones_adicionales=data.certificaciones_adicionales,
        telefono=data.telefono,
        email=data.email,
        direccion=data.direccion,
        pais=data.pais,
        ciudad=data.ciudad,
        codigo_postal=data.codigo_postal,
        estado=data.estado.value,  # Igual aquí .value
        motivo_suspension=data.motivo_suspension,
        foto_perfil_url=data.foto_perfil_url,
        fecha_registro=datetime.now(),
        id_turno=1  # Si quieres, también puedes pedirlo en el esquema
    )
    db.add(nuevo_medico)
    await db.commit()
    await db.refresh(nuevo_medico)
    return nuevo_medico

#Registrar paciente
async def crear_paciente(data: PacienteCreate, db: AsyncSession):
    nuevo_paciente = Paciente(
        nombre=data.nombre,
        apellido=data.apellido,
        fecha_nacimiento=data.fecha_nacimiento,
        genero_id=data.genero_id,
        direccion=data.direccion,
        telefono=data.telefono,
        email=data.email,
        historial_medico_id=data.historial_medico_id,
        alergias_id=data.alergias_id,
        antecedentes_familiares_id=data.antecedentes_familiares_id,
        historial_farmacos_id=data.historial_farmacos_id,
        estado_id=data.estado_id,
        fecha_registro=datetime.now()
    )
    db.add(nuevo_paciente)
    await db.commit()
    await db.refresh(nuevo_paciente)
    return nuevo_paciente

#Buscador 
async def filtro_pacientes(filtro: PacienteFiltroRequest, db: AsyncSession):
    stmt = select(Paciente)
    condiciones = []

    if filtro.paciente_id:
        condiciones.append(Paciente.paciente_id == filtro.paciente_id)
    if filtro.nombre:
        condiciones.append(Paciente.nombre.ilike(f"%{filtro.nombre}%"))
    if filtro.apellido:
        condiciones.append(Paciente.apellido.ilike(f"%{filtro.apellido}%"))
    if filtro.fecha_nacimiento:
        condiciones.append(Paciente.fecha_nacimiento == filtro.fecha_nacimiento)
    if filtro.genero_id:
        condiciones.append(Paciente.genero_id == filtro.genero_id)
    if filtro.direccion:
        condiciones.append(Paciente.direccion.ilike(f"%{filtro.direccion}%"))
    if filtro.telefono:
        condiciones.append(Paciente.telefono.ilike(f"%{filtro.telefono}%"))
    if filtro.email:
        condiciones.append(Paciente.email.ilike(f"%{filtro.email}%"))
    if filtro.fecha_registro:
        condiciones.append(Paciente.fecha_registro == filtro.fecha_registro)
    if filtro.historial_medico_id:
        condiciones.append(Paciente.historial_medico_id == filtro.historial_medico_id)
    if filtro.alergias_id:
        condiciones.append(Paciente.alergias_id == filtro.alergias_id)
    if filtro.antecedentes_familiares_id:
        condiciones.append(Paciente.antecedentes_familiares_id == filtro.antecedentes_familiares_id)
    if filtro.historial_farmacos_id:
        condiciones.append(Paciente.historial_farmacos_id == filtro.historial_farmacos_id)
    if filtro.estado_id:
        condiciones.append(Paciente.estado_id == filtro.estado_id)

    if condiciones:
        stmt = stmt.where(and_(*condiciones))

    result = await db.execute(stmt)
    return result.scalars().all()

#Get all pacinetes 
async def get_pacientes_all(db:AsyncSession):
    stmt=select(Paciente)
    result=await db.execute(stmt)
    pacientes_mod=result.scalars().first()
    if not pacientes_mod:
        raise HTTPException(status_code=401, detail="No hay datos")
    return pacientes_mod
    
#Nuevo medico 
async def get_medicos(db: AsyncSession):
    stmt=select(MedicosModel)
    result= await db.execute(stmt)
    items=result.scalars().all()
    if not items:
        raise HTTPException(status_code=401, detail="No hay datos")
    return items

#NEW USER MED
async def new_user_med(usuario:MedUserSchema,db:AsyncSession):
    stmt = select(MedUser).where(MedUser.st_usuario == usuario.st_usuario)
    result = await db.execute(stmt)
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya está registrado")
    
    nuevo_usuario = MedUser(
        id_medico=usuario.id_medico,
        st_usuario=usuario.st_usuario,
        st_token=usuario.st_token,
        id_rol_usuario=usuario.id_rol_usuario,
        id_activo=usuario.id_activo,
        dt_fecha_registro=usuario.dt_fecha_registro,
        id_membresia=usuario.id_membresia,
    )
    db.add(nuevo_usuario)

    await db.commit()
    await db.refresh(nuevo_usuario)
 
    return nuevo_usuario