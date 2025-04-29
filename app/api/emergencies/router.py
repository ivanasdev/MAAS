"""

*Authors:Ivn Acsuart, PMJ(Paca, Manolito, Joselito, Maia y Nina mis leales coautores)
*Created at:23-04-5
*Name System:MedsAPI
*Module:Emergencies

"""



from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

#DB
from core.db import get_db
#Schemas
from schemas.meds_schema import MedicoLoginRequest
#Auth
from core.crud import get_users_auth
from services.jwt_create_token import crear_token2
#Response maker
from services.reponses import response_user


router = APIRouter(prefix="/emergencies")


@router.get("/")
async def eme_api():
    return {"msg":"ok"}

@router.post("/access1")
async def login_medico(request: MedicoLoginRequest,db: AsyncSession = Depends(get_db)):
    user = await get_users_auth(request, db) 
    token_access=crear_token2(user)
    respuesta=response_user(user,token_access)    
    return respuesta
