-- ============================================
-- Esquema clínico mínimo
-- Tablas: paciente, medicion_pa, labs_diabetes
-- ============================================

-- Tabla de pacientes
CREATE TABLE paciente (
  paciente_id SERIAL PRIMARY KEY,          -- Identificador único autoincremental
  documento TEXT UNIQUE,                   -- Documento ficticio, no repetido
  nombre TEXT,                             -- Nombre del paciente
  sexo TEXT CHECK (sexo IN ('F','M','X')), -- Restricción: solo F, M o X
  fecha_nacimiento DATE                    -- Fecha de nacimiento
);

-- Tabla de mediciones de presión arterial
CREATE TABLE medicion_pa (
  medicion_id SERIAL PRIMARY KEY,          -- Identificador único de la medición
  paciente_id INTEGER NOT NULL REFERENCES paciente(paciente_id), -- Relación con paciente
  fecha TIMESTAMP NOT NULL,                -- Fecha y hora de la medición
  sistolica INTEGER CHECK (sistolica BETWEEN 60 AND 260), -- Validación de rango clínico
  diastolica INTEGER CHECK (diastolica BETWEEN 40 AND 150), -- Validación de rango clínico
  metodo TEXT CHECK (metodo IN ('manual','automatica')) -- Método de medición
);

-- Índice para acelerar consultas por paciente y fecha
CREATE INDEX idx_medicion_pa_paciente_fecha
  ON medicion_pa (paciente_id, fecha);

-- Tabla de laboratorios de diabetes
CREATE TABLE labs_diabetes (
  lab_id SERIAL PRIMARY KEY,               -- Identificador único del análisis
  patient_id INTEGER NOT NULL REFERENCES paciente(paciente_id), -- Relación con paciente
  fecha TIMESTAMP NOT NULL,                -- Fecha y hora del análisis
  glucemia_ayunas INTEGER CHECK (glucemia_ayunas BETWEEN 60 AND 300), -- mg/dL
  glucemia_postprandial INTEGER CHECK (glucemia_postprandial BETWEEN 80 AND 400), -- mg/dL
  hba1c NUMERIC(4,2) CHECK (hba1c BETWEEN 4.0 AND 15.0), -- % con 2 decimales
  metodo TEXT CHECK (metodo IN ('enzimatico','HPLC')) -- Método de laboratorio
);

-- ============================================
-- Fin del esquema clínico mínimo
-- ============================================
