#script rápido probar_conexion.py para probar:
from conexion_supabase import engine, test_connection
from sqlalchemy import text

print("Probando conexión...")
print("Hora desde la DB:", test_connection())

with engine.connect() as conn:
    version = conn.execute(text("select version()")).scalar()
    print("Versión de PostgreSQL:", version)
