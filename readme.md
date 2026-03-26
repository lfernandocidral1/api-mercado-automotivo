# API Clientes e Mercado Automotivo

API REST com FastAPI + SQLAlchemy + SQLite  
Dados de SUVs baseados na Fenabrave — Janeiro e Fevereiro de 2025.

## Como rodar o projeto

1. Instalar dependências:
```
pip install -r requirements.txt
```

2. Rodar o servidor:
```
py -3.12 -m uvicorn main:app --reload --port 8001
```

3. Acessar no navegador:
```
http://127.0.0.1:8001/docs
```

## SUVs cadastrados

| Modelo | Janeiro | Fevereiro |
|--------|---------|-----------|
| Toyota RAV4 | 3.850 | 4.120 |
| Jeep Compass | 3.620 | 3.890 |
| Volkswagen T-Cross | 3.410 | 3.650 |
| Chevrolet Tracker | 3.180 | 3.420 |
| Hyundai Creta | 2.950 | 3.210 |