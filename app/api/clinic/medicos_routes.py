"""

*Authors:Ivn Acsuart, PMJ(Paca, Manolito, Joselito, Maia y Nina mis leales coautores)
*Created at:18-04-5
*Name System:MedsAPI
*Module:Clinic

"""
#Config imports 
from fastapi import APIRouter, HTTPException,Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
#Schemas
from schemas.meds_schema import MedicoLoginRequest, MedUserSchema,MedicoCreate

#Auth
from core.db import get_db
from core.crud import get_users_auth,new_user_med,get_medicos,crear_medico
from services.jwt_create_token import crear_token2
#Services
from services.reponses import response_user


router = APIRouter(prefix="/clinic/medicos")

#Home Routes 
@router.get("/")
async def home():
    return {"message": "Bienvenido a la API de Medicos "}

#Get medicos
@router.get("/get_medics")
async def get_all_medicos(db: AsyncSession = Depends(get_db)):
    getmed=await get_medicos(db)
    return getmed
    
#Registrar medico 
@router.post("/registro")
async def registrar_medico(medico: MedicoCreate, db: AsyncSession = Depends(get_db)):
    try:
        nuevo = await crear_medico(medico, db)
        return {
            "message": "Médico registrado con éxito",
            "id_medico": nuevo.id_medico
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar: {str(e)}")


