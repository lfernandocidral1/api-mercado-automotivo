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
            SUV(marca="Volkswagen",  modelo="T-Cross",          ano=2026, vendas_janeiro=5741, vendas_fevereiro=5667, preco=159900.0),
            SUV(marca="Volkswagen",  modelo="Tera",              ano=2026, vendas_janeiro=4992, vendas_fevereiro=5338, preco=134900.0),
            SUV(marca="Hyundai",     modelo="Creta",             ano=2026, vendas_janeiro=4428, vendas_fevereiro=5045, preco=149900.0),
            SUV(marca="Jeep",        modelo="Compass",           ano=2026, vendas_janeiro=4503, vendas_fevereiro=4169, preco=198900.0),
            SUV(marca="Chevrolet",   modelo="Tracker",           ano=2026, vendas_janeiro=4532, vendas_fevereiro=4003, preco=162900.0),
            SUV(marca="Fiat",        modelo="Fastback",          ano=2026, vendas_janeiro=3927, vendas_fevereiro=3833, preco=144900.0),
            SUV(marca="BYD",         modelo="Song",              ano=2026, vendas_janeiro=3802, vendas_fevereiro=3702, preco=189900.0),
            SUV(marca="Volkswagen",  modelo="Nivus",             ano=2026, vendas_janeiro=3167, vendas_fevereiro=3851, preco=139900.0),
            SUV(marca="Fiat",        modelo="Pulse",             ano=2026, vendas_janeiro=3193, vendas_fevereiro=3057, preco=114900.0),
            SUV(marca="Nissan",      modelo="Kicks",             ano=2026, vendas_janeiro=3058, vendas_fevereiro=2875, preco=144900.0),
            SUV(marca="GWM",         modelo="Haval H6",          ano=2026, vendas_janeiro=2627, vendas_fevereiro=3237, preco=219900.0),
            SUV(marca="Jeep",        modelo="Renegade",          ano=2026, vendas_janeiro=3052, vendas_fevereiro=2686, preco=169900.0),
            SUV(marca="Honda",       modelo="HR-V",              ano=2026, vendas_janeiro=2773, vendas_fevereiro=2948, preco=189900.0),
            SUV(marca="Toyota",      modelo="Corolla Cross",     ano=2026, vendas_janeiro=2176, vendas_fevereiro=2899, preco=219900.0),
            SUV(marca="Honda",       modelo="WR-V",              ano=2026, vendas_janeiro=1811, vendas_fevereiro=2630, preco=134900.0),
            SUV(marca="Caoa Chery",  modelo="Tiggo 7",           ano=2026, vendas_janeiro=1937, vendas_fevereiro=2205, preco=179900.0),
            SUV(marca="Jeep",        modelo="Commander",         ano=2026, vendas_janeiro=1330, vendas_fevereiro=1371, preco=289900.0),
            SUV(marca="Renault",     modelo="Kardian",           ano=2026, vendas_janeiro=1310, vendas_fevereiro=1122, preco=124900.0),
            SUV(marca="Toyota",      modelo="Hilux SW4",         ano=2026, vendas_janeiro=1230, vendas_fevereiro=1031, preco=389900.0),
            SUV(marca="Volkswagen",  modelo="Taos",              ano=2026, vendas_janeiro=1225, vendas_fevereiro=1022, preco=219900.0),
            SUV(marca="Omoda",       modelo="Jaecoo Omoda 5",    ano=2026, vendas_janeiro=1067, vendas_fevereiro=1179, preco=189900.0),
            SUV(marca="Caoa Chery",  modelo="Tiggo 8",           ano=2026, vendas_janeiro=1271, vendas_fevereiro=973,  preco=229900.0),
            SUV(marca="Citroen",     modelo="Basalt",            ano=2026, vendas_janeiro=1027, vendas_fevereiro=971,  preco=129900.0),
            SUV(marca="Nissan",      modelo="Kait",              ano=2026, vendas_janeiro=644,  vendas_fevereiro=1294, preco=159900.0),
            SUV(marca="Renault",     modelo="Duster",            ano=2026, vendas_janeiro=936,  vendas_fevereiro=951,  preco=119900.0),
            SUV(marca="GWM",         modelo="Haval H9",          ano=2026, vendas_janeiro=882,  vendas_fevereiro=672,  preco=389900.0),
            SUV(marca="Ford",        modelo="Territory",         ano=2026, vendas_janeiro=851,  vendas_fevereiro=682,  preco=249900.0),
            SUV(marca="Peugeot",     modelo="2008",              ano=2026, vendas_janeiro=703,  vendas_fevereiro=561,  preco=169900.0),
            SUV(marca="Renault",     modelo="Boreal",            ano=2026, vendas_janeiro=641,  vendas_fevereiro=611,  preco=134900.0),
            SUV(marca="Mitsubishi",  modelo="Eclipse Cross",     ano=2026, vendas_janeiro=560,  vendas_fevereiro=555,  preco=249900.0),
            SUV(marca="BYD",         modelo="Yuan",              ano=2026, vendas_janeiro=525,  vendas_fevereiro=545,  preco=199900.0),
            SUV(marca="Omoda",       modelo="Jaecoo 7",          ano=2026, vendas_janeiro=14,   vendas_fevereiro=458,  preco=219900.0),
            SUV(marca="GAC",         modelo="GS4",               ano=2026, vendas_janeiro=488,  vendas_fevereiro=309,  preco=179900.0),
            SUV(marca="Toyota",      modelo="RAV4",              ano=2026, vendas_janeiro=488,  vendas_fevereiro=299,  preco=279900.0),
            SUV(marca="GWM",         modelo="Tank 300",          ano=2026, vendas_janeiro=363,  vendas_fevereiro=423,  preco=499900.0),
            SUV(marca="Leapmotor",   modelo="C10",               ano=2026, vendas_janeiro=441,  vendas_fevereiro=304,  preco=219900.0),
            SUV(marca="Toyota",      modelo="Yaris Cross",       ano=2026, vendas_janeiro=14,   vendas_fevereiro=393,  preco=169900.0),
            SUV(marca="Citroen",     modelo="Aircross",          ano=2026, vendas_janeiro=290,  vendas_fevereiro=316,  preco=144900.0),
            SUV(marca="BMW",         modelo="X1",                ano=2026, vendas_janeiro=276,  vendas_fevereiro=319,  preco=389900.0),
            SUV(marca="Caoa Chery",  modelo="Tiggo 5X",          ano=2026, vendas_janeiro=305,  vendas_fevereiro=207,  preco=159900.0),
        ]
        db.add_all(suvs)
        db.commit()
        print("Dados de 40 SUVs inseridos com sucesso!")
    except Exception as e:
        db.rollback()
        print(f"Erro ao inserir dados: {e}")
    finally:
        db.close()