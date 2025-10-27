from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import psycopg2

app = FastAPI(title="Portal del Lago API")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend Portal del Lago activo y funcionando correctamente."}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        conn.close()
        return {"status": "OK", "db_time": result[0]}
    except Exception as e:
        return {"status": "ERROR", "detail": str(e)}
