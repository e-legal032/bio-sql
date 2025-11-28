import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("es_ES")
random.seed(42)

# Número de pacientes y mediciones
N_PATIENTS = 50
N_MEDICIONES = 200
N_LABS = 100

# --- Pacientes ---
patients = []
for pid in range(1, N_PATIENTS+1):
    birth_date = fake.date_of_birth(minimum_age=20, maximum_age=90)
    patients.append({
        "patient_id": pid,
        "nombre": fake.first_name(),
        "apellido": fake.last_name(),
        "fecha_nacimiento": birth_date,
        "sexo": random.choice(["F","M","X"]),
        "fumador": random.choice([True, False]),
        "diabetes": random.choice([True, False]),
        "obesidad": random.choice([True, False])
    })

# --- Mediciones de presión arterial ---
mediciones = []
for mid in range(1, N_MEDICIONES+1):
    paciente = random.choice(patients)
    fecha = datetime.now() - timedelta(days=random.randint(0, 365))
    sistolica = random.randint(90, 180)
    diastolica = random.randint(60, 110)
    mediciones.append({
        "medicion_id": mid,
        "patient_id": paciente["patient_id"],
        "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
        "sistolica": sistolica,
        "diastolica": diastolica,
        "metodo": random.choice(["manual","automatica"])
    })

# --- Laboratorios de diabetes ---
labs = []
for lid in range(1, N_LABS+1):
    paciente = random.choice(patients)
    fecha = datetime.now() - timedelta(days=random.randint(0, 365))
    glucemia_ayunas = random.randint(70, 160)
    glucemia_post = random.randint(90, 250)
    hba1c = round(random.uniform(4.5, 9.5), 2)
    labs.append({
        "lab_id": lid,
        "patient_id": paciente["patient_id"],
        "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
        "glucemia_ayunas": glucemia_ayunas,
        "glucemia_postprandial": glucemia_post,
        "hba1c": hba1c
    })

# Exportar a CSV
pd.DataFrame(patients).to_csv("data/patients.csv", index=False)
pd.DataFrame(mediciones).to_csv("data/mediciones.csv", index=False)
pd.DataFrame(labs).to_csv("data/labs.csv", index=False)

print("Datasets generados en carpeta data/")
