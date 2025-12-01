"""
📦 Módulo: conexion_supabase.py
🧠 Propósito: Conexión segura y centralizada a Supabase usando SQLAlchemy
✍️ Autoría: Ana Sposito
🗓️ Fecha: Diciembre 2025
"""
from dotenv import load_dotenv
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text
import os

# 🔐 Cargar variables desde .env
load_dotenv()

user = os.getenv("SUPABASE_USER")
raw_password = os.getenv("SUPABASE_PASSWORD")
host = os.getenv("SUPABASE_HOST")
port = os.getenv("SUPABASE_PORT")
db = os.getenv("SUPABASE_DB")

# ✅ Validaciones mínimas (evita errores silenciosos)
missing = [k for k, v in {
    "SUPABASE_USER": user,
    "SUPABASE_PASSWORD": raw_password,
    "SUPABASE_HOST": host,
    "SUPABASE_PORT": port,
    "SUPABASE_DB": db,
}.items() if not v]

if missing:
    raise RuntimeError(f"Faltan variables en .env: {', '.join(missing)}")

# 🔏 Encode de password para URI (maneja espacios y símbolos especiales)
encoded_password = quote_plus(raw_password)

# 🔗 URI segura (Transaction Pooler)
URI = f"postgresql://{user}:{encoded_password}@{host}:{port}/{db}"

# 🚀 Crear motor de conexión
engine = create_engine(URI, pool_pre_ping=True, pool_recycle=1800)

def test_connection():
    """
    Ejecuta un SELECT básico para validar la conexión.
    """
    with engine.connect() as conn:
        return conn.execute(text("select now()")).scalar()

