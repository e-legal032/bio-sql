"""
Modelo ORM clínico en SQLAlchemy 2.0
Tablas: paciente, medicion_pa, labs_diabetes
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, DateTime, ForeignKey, Numeric, CheckConstraint, Index


# Base declarativa (registra todas las tablas)
class Base(DeclarativeBase):
    pass


# 👤 Tabla de pacientes
class Paciente(Base):
    __tablename__ = "paciente"

    patient_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String)
    apellido: Mapped[str] = mapped_column(String)
    fecha_nacimiento: Mapped[Date] = mapped_column(Date)
    sexo: Mapped[str] = mapped_column(String)
    fumador: Mapped[str] = mapped_column(String)   # Podrías usar Boolean si tus CSV tienen True/False
    diabetes: Mapped[str] = mapped_column(String)
    obesidad: Mapped[str] = mapped_column(String)

    mediciones: Mapped[list["MedicionPA"]] = relationship(back_populates="paciente", cascade="all, delete-orphan")
    labs: Mapped[list["LabsDiabetes"]] = relationship(back_populates="paciente", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("sexo IN ('F','M','X')", name="paciente_sexo_chk"),
    )


# 💓 Tabla de mediciones de presión arterial
class MedicionPA(Base):
    __tablename__ = "medicion_pa"

    medicion_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("paciente.patient_id"), nullable=False)
    fecha: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    sistolica: Mapped[int] = mapped_column(Integer)
    diastolica: Mapped[int] = mapped_column(Integer)
    metodo: Mapped[str] = mapped_column(String)

    paciente: Mapped["Paciente"] = relationship(back_populates="mediciones")

    __table_args__ = (
        CheckConstraint("sistolica BETWEEN 60 AND 260", name="pa_sistolica_chk"),
        CheckConstraint("diastolica BETWEEN 40 AND 150", name="pa_diastolica_chk"),
        CheckConstraint("metodo IN ('manual','automatica')", name="pa_metodo_chk"),
        Index("idx_medicion_pa_patient_fecha", "patient_id", "fecha"),
    )


# 🧪 Tabla de laboratorios de diabetes
class LabsDiabetes(Base):
    __tablename__ = "labs_diabetes"

    lab_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("paciente.patient_id"), nullable=False)
    fecha: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    glucemia_ayunas: Mapped[int] = mapped_column(Integer)
    glucemia_postprandial: Mapped[int] = mapped_column(Integer)
    hba1c: Mapped[Numeric] = mapped_column(Numeric(4, 2))

    paciente: Mapped["Paciente"] = relationship(back_populates="labs")

    __table_args__ = (
        CheckConstraint("glucemia_ayunas BETWEEN 60 AND 300", name="labs_ga_chk"),
        CheckConstraint("glucemia_postprandial BETWEEN 80 AND 400", name="labs_gp_chk"),
        CheckConstraint("hba1c BETWEEN 4.0 AND 15.0", name="labs_hba1c_chk"),
    )
