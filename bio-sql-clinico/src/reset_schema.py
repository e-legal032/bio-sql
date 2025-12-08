"""
🗑️ Script auxiliar: reset_schema.py
Propósito: eliminar todas las tablas definidas en el ORM y recrear el esquema limpio.
"""

from src import Base, engine

if __name__ == "__main__":
    print("⚠️ Eliminando todas las tablas del esquema...")
    Base.metadata.drop_all(engine)
    print("🗑️ Esquema eliminado. Ahora podés volver a correr `python -m src.main` para recrear las tablas.")
