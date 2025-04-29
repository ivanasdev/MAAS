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
from schemas.meds_schema import MedicoLoginRequest, MedUserSchema
#DB
from core.db import engine,get_db
#Auth
from core.crud import get_users_auth,new_user_med
from services.jwt_create_token import crear_token2
#Services
from services.reponses import response_user


router = APIRouter(prefix="/clinic")

#Home Routes 
@router.get("/")
async def home():
    return {"message": "Bienvenido a la MEDSAPI"}

#loginClinic
@router.post("/access2")
async def login_medico(request: MedicoLoginRequest,db: AsyncSession = Depends(get_db)):
    user = await get_users_auth(request, db) 
    if user:
        print(user.st_usuario)
        token_access=crear_token2(user)
        respuesta=response_user(user,token_access)    
        return respuesta


#Creates new user system 
@router.post("/new_med_user")
async def registrar_usuario(usuario: MedUserSchema, db: AsyncSession = Depends(get_db)):
    new_user= await new_user_med(usuario,db)
    return new_user
   



   



