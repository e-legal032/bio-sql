"""
Carga de CSVs (patients, mediciones, labs) a Supabase con pandas.to_sql
Profesional: usa SQLAlchemy Core + chunksize para inserción por lotes
"""

import os
import pandas as pd
from src.conexion_supabase import engine

# 📂 Directorio de datos
ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(ROOT), "data")

def load_patients():
    df = pd.read_csv(os.path.join(DATA, "patients.csv"))
    expected = {"patient_id", "nombre", "apellido", "fecha_nacimiento", "sexo", "fumador", "diabetes", "obesidad"}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas en patients.csv: {missing}")
    # Si patient_id está en el CSV, se inserta tal cual (coincide con ORM)
    df.to_sql("paciente", engine, if_exists="append", index=False, chunksize=500)
    print(f"✅ pacientes: {len(df)} filas cargadas")

def load_mediciones():
    df = pd.read_csv(os.path.join(DATA, "mediciones.csv"))
    expected = {"medicion_id", "patient_id", "fecha", "sistolica", "diastolica", "metodo"}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas en mediciones.csv: {missing}")
    df.to_sql("medicion_pa", engine, if_exists="append", index=False, chunksize=500)
    print(f"✅ mediciones: {len(df)} filas cargadas")

def load_labs():
    df = pd.read_csv(os.path.join(DATA, "labs.csv"))
    expected = {"lab_id", "patient_id", "fecha", "glucemia_ayunas", "glucemia_postprandial", "hba1c"}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas en labs.csv: {missing}")
    df.to_sql("labs_diabetes", engine, if_exists="append", index=False, chunksize=500)
    print(f"✅ labs: {len(df)} filas cargadas")


if __name__ == "__main__":
    load_patients()
    load_mediciones()
    load_labs()
