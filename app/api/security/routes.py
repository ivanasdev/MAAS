from fastapi import APIRouter
from api.security.faceid.services  import abrir_camara_y_grabar,abrir_camara_reconocimiento
import threading


router = APIRouter(prefix="/safecam")



#Home Routes 
@router.get("/o")
async def opencam():
    cam01=  abrir_camara_y_grabar()
    return cam01



@router.get("/abrir-camara")
def abrir_camara_endpoint():
    # Abrimos la cámara en un thread para que FastAPI no se bloquee
    threading.Thread(target=abrir_camara_reconocimiento).start()
    return {"message": "Cámara abierta para reconocimiento facial"}



