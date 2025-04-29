"""

*Authors:Ivn Acsuart, Paca, Manolito, Joselito, Maia y Nina mis leales y amados coautores)
*Created at:18-04-5
*Name System:MedsAPI
*Module:Clinic

"""
#Config imports 
from fastapi import APIRouter, HTTPException,Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
#DB
from core.db import engine,get_db

#CRUD
from core.crud import get_pacientes_all,filtro_pacientes,crear_paciente
from services.reponses import response_get_pacientes,response_create_pacientes

#smodels
from schemas.pacientes_schema import PacienteFiltroRequest,PacienteCreate

router = APIRouter(prefix="/clinic/pacientes")

#Home Routes 
@router.get("/")
async def home():
    return {"message": "Bienvenido a la api pacientes"}

#Get all pacientes
@router.get("/get_pacientes")
async def new_pac(db: AsyncSession = Depends(get_db)):
    patient = await get_pacientes_all(db)
    resp_pac=response_get_pacientes(patient=patient)
    return resp_pac

#Buscador con filtros de pacientes 
@router.post("/buscador")
async def obtener_pacientes_filtro(filtro: PacienteFiltroRequest, db: AsyncSession = Depends(get_db)):
    pacientes = await filtro_pacientes(filtro, db)
    return pacientes

#New Patient
@router.post("/registro")
async def registrar_paciente(paciente: PacienteCreate, db: AsyncSession = Depends(get_db)):
    nuevop = await crear_paciente(paciente, db)
    resp_conf= response_create_pacientes(nuevop)
    return resp_conf