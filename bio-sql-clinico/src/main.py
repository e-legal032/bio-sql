from src import Base, engine

Base.metadata.create_all(engine)
print("✅ Tablas creadas en Supabase")
