# Diccionario de datos clínicos /Variables Map/

## Tabla pacientes
- patient_id: Identificador único
- nombre, apellido
- fecha_nacimiento
- sexo (F/M/X)
- factores de riesgo: fumador, diabetes, obesidad

## Tabla mediciones presión arterial
- medicion_id
- patient_id (FK)
- fecha
- sistolica (mmHg)
- diastolica (mmHg)
- metodo (manual/automatica)

## Tabla laboratorios diabetes
- lab_id
- patient_id (FK)
- fecha
- glucemia_ayunas (mg/dL)
- glucemia_postprandial (mg/dL)
- hba1c (%)
