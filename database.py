from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./mercado_automotivo.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    cidade = Column(String, nullable=False)
    telefone = Column(String, nullable=True)


class SUV(Base):
    __tablename__ = "suvs"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    vendas_janeiro = Column(Integer, nullable=False)
    vendas_fevereiro = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)


def seed_data():
    db = SessionLocal()
    try:
        if db.query(SUV).count() > 0:
            return
        suvs = [
            SUV(marca="Toyota", modelo="RAV4", ano=2024, vendas_janeiro=3850, vendas_fevereiro=4120, preco=219900.0),
            SUV(marca="Jeep", modelo="Compass", ano=2024, vendas_janeiro=3620, vendas_fevereiro=3890, preco=198900.0),
            SUV(marca="Volkswagen", modelo="T-Cross", ano=2024, vendas_janeiro=3410, vendas_fevereiro=3650, preco=159900.0),
            SUV(marca="Chevrolet", modelo="Tracker", ano=2024, vendas_janeiro=3180, vendas_fevereiro=3420, preco=162900.0),
            SUV(marca="Hyundai", modelo="Creta", ano=2024, vendas_janeiro=2950, vendas_fevereiro=3210, preco=149900.0),
        ]
        db.add_all(suvs)
        db.commit()
        print("Dados de SUVs inseridos com sucesso!")
    except Exception as e:
        db.rollback()
        print(f"Erro ao inserir dados: {e}")
    finally:
        db.close()