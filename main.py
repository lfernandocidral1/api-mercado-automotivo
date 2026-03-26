from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db, create_tables, seed_data, Cliente, SUV
from schemas import (
    ClienteCreate, ClienteUpdate, ClienteResponse,
    SUVResponse, SUVRanking, SUVCrescimento, SUVMarketShare, SUVComparativo
)

app = FastAPI(
    title="API Clientes e Mercado Automotivo",
    description="API para gestão de clientes e análise do mercado de SUVs - dados Fenabrave Jan/Fev 2025",
    version="0.1.0"
)


@app.on_event("startup")
def startup():
    create_tables()
    seed_data()


@app.get("/clientes", response_model=List[ClienteResponse], tags=["default"], summary="Listar Clientes")
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()


@app.post("/clientes", response_model=ClienteResponse, status_code=201, tags=["default"], summary="Criar Cliente")
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    existente = db.query(Cliente).filter(Cliente.email == cliente.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    novo = Cliente(**cliente.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.get("/clientes/filtro", response_model=List[ClienteResponse], tags=["default"], summary="Filtrar Clientes Por Cidade")
def filtrar_por_cidade(cidade: str, db: Session = Depends(get_db)):
    return db.query(Cliente).filter(Cliente.cidade.ilike(f"%{cidade}%")).all()


@app.get("/clientes/{cliente_id}", response_model=ClienteResponse, tags=["default"], summary="Buscar Cliente")
def buscar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return cliente


@app.put("/clientes/{cliente_id}", response_model=ClienteResponse, tags=["default"], summary="Atualizar Cliente")
def atualizar_cliente(cliente_id: int, dados: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(cliente, campo, valor)
    db.commit()
    db.refresh(cliente)
    return cliente


@app.delete("/clientes/{cliente_id}", tags=["default"], summary="Deletar Cliente")
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    db.delete(cliente)
    db.commit()
    return {"mensagem": f"Cliente {cliente_id} removido com sucesso."}


@app.get("/suvs", response_model=List[SUVResponse], tags=["default"], summary="Listar Suvs")
def listar_suvs(db: Session = Depends(get_db)):
    return db.query(SUV).all()


@app.get("/suvs/ranking", response_model=List[SUVRanking], tags=["default"], summary="Ranking Suvs")
def ranking_suvs(db: Session = Depends(get_db)):
    suvs = db.query(SUV).all()
    total_geral = sum(s.vendas_janeiro + s.vendas_fevereiro for s in suvs)
    resultado = sorted(
        [{"posicao": 0, "marca": s.marca, "modelo": s.modelo,
          "total_vendas": s.vendas_janeiro + s.vendas_fevereiro,
          "marketshare": round((s.vendas_janeiro + s.vendas_fevereiro) / total_geral * 100, 2)}
         for s in suvs],
        key=lambda x: x["total_vendas"], reverse=True
    )
    for i, item in enumerate(resultado):
        item["posicao"] = i + 1
    return resultado


@app.get("/suvs/crescimento", response_model=List[SUVCrescimento], tags=["default"], summary="Crescimento Suvs")
def crescimento_suvs(db: Session = Depends(get_db)):
    suvs = db.query(SUV).all()
    resultado = []
    for s in suvs:
        crescimento = ((s.vendas_fevereiro - s.vendas_janeiro) / s.vendas_janeiro * 100) if s.vendas_janeiro > 0 else 0.0
        resultado.append({"marca": s.marca, "modelo": s.modelo,
                          "vendas_janeiro": s.vendas_janeiro, "vendas_fevereiro": s.vendas_fevereiro,
                          "crescimento_percentual": round(crescimento, 2)})
    return sorted(resultado, key=lambda x: x["crescimento_percentual"], reverse=True)


@app.get("/suvs/top3", response_model=List[SUVRanking], tags=["default"], summary="Top3 Suvs")
def top3_suvs(db: Session = Depends(get_db)):
    suvs = db.query(SUV).all()
    total_geral = sum(s.vendas_janeiro + s.vendas_fevereiro for s in suvs)
    resultado = sorted(
        [{"posicao": 0, "marca": s.marca, "modelo": s.modelo,
          "total_vendas": s.vendas_janeiro + s.vendas_fevereiro,
          "marketshare": round((s.vendas_janeiro + s.vendas_fevereiro) / total_geral * 100, 2)}
         for s in suvs],
        key=lambda x: x["total_vendas"], reverse=True
    )[:3]
    for i, item in enumerate(resultado):
        item["posicao"] = i + 1
    return resultado


@app.get("/suvs/marketshare", response_model=List[SUVMarketShare], tags=["default"], summary="Marketshare Suvs")
def marketshare_suvs(db: Session = Depends(get_db)):
    suvs = db.query(SUV).all()
    total_geral = sum(s.vendas_janeiro + s.vendas_fevereiro for s in suvs)
    return sorted(
        [{"marca": s.marca, "modelo": s.modelo,
          "vendas_totais": s.vendas_janeiro + s.vendas_fevereiro,
          "marketshare_percentual": round((s.vendas_janeiro + s.vendas_fevereiro) / total_geral * 100, 2)}
         for s in suvs],
        key=lambda x: x["marketshare_percentual"], reverse=True
    )


@app.get("/suvs/comparativo", response_model=List[SUVComparativo], tags=["default"], summary="Comparativo Suvs")
def comparativo_suvs(db: Session = Depends(get_db)):
    suvs = db.query(SUV).all()
    return [{"marca": s.marca, "modelo": s.modelo,
             "vendas_janeiro": s.vendas_janeiro, "vendas_fevereiro": s.vendas_fevereiro,
             "variacao": s.vendas_fevereiro - s.vendas_janeiro}
            for s in suvs]


@app.get("/teste", tags=["default"], summary="Rota Teste")
def rota_teste():
    return {"status": "ok", "mensagem": "API Mercado Automotivo rodando com sucesso!"}