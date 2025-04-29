from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.clinic.medicos_routes import router as cli_medicos
from api.clinic.router import router as clinic_router
from api.emergencies.router import router as emergencies
from api.clinic.pacientes_routes import router as pacientes

app = FastAPI()

# CONFIGURAR CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Aquí pones el frontend permitido
    allow_credentials=True,
    allow_methods=["*"],  # Puedes restringir si quieres solo POST, GET, etc.
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(clinic_router)
app.include_router(emergencies)
app.include_router(cli_medicos)
app.include_router(pacientes)
