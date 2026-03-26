from pydantic import BaseModel
from typing import Optional


class ClienteBase(BaseModel):
    nome: str
    email: str
    cidade: str
    telefone: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    cidade: Optional[str] = None
    telefone: Optional[str] = None


class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True


class SUVBase(BaseModel):
    marca: str
    modelo: str
    ano: int
    vendas_janeiro: int
    vendas_fevereiro: int
    preco: float


class SUVResponse(SUVBase):
    id: int

    class Config:
        from_attributes = True


class SUVRanking(BaseModel):
    posicao: int
    marca: str
    modelo: str
    total_vendas: int
    marketshare: float


class SUVCrescimento(BaseModel):
    marca: str
    modelo: str
    vendas_janeiro: int
    vendas_fevereiro: int
    crescimento_percentual: float


class SUVMarketShare(BaseModel):
    marca: str
    modelo: str
    vendas_totais: int
    marketshare_percentual: float


class SUVComparativo(BaseModel):
    marca: str
    modelo: str
    vendas_janeiro: int
    vendas_fevereiro: int
    variacao: int