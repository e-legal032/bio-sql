"""
📦 Paquete: src
🧠 Propósito: Punto de entrada del código clínico con conexión a Supabase y modelos ORM
✍️ Autoría: Ana Sposito
🗓️ Fecha: Diciembre 2025
"""

# Reexportar lo más usado
from .conexion_supabase import engine, test_connection
from .schema_orm import Base, Paciente, MedicionPA, LabsDiabetes

__all__ = [
    "engine",
    "test_connection",
    "Base",
    "Paciente",
    "MedicionPA",
    "LabsDiabetes",
]
