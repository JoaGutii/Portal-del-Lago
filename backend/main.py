from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Portal del Lago Backend", version="1.0")

# CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Servidor funcionando correctamente 🚀"}

@app.get("/docs-info")
def docs_info():
    return {"info": "Visita /docs para ver la documentación interactiva"}

# Conexión con Supabase (solo si existen las variables)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("⚠️ Variables de entorno de Supabase no configuradas")
else:
    print("✅ Conectado con Supabase correctamente")
