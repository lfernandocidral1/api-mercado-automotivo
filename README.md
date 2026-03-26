# API Clientes e Mercado Automotivo

API REST com FastAPI + SQLAlchemy + SQLite  
Dados de SUVs baseados na Fenabrave — Janeiro e Fevereiro de 2026.

## Como rodar o projeto

1. Instalar dependências:
```
py -3.12 -m pip install -r requirements.txt
```

2. Rodar o servidor:
```
py -3.12 -m uvicorn main:app --reload --port 8001
```

3. Acessar no navegador:
```
http://127.0.0.1:8001/docs
```

## Top 10 SUVs mais vendidos (Fenabrave Jan/Fev 2026)

| Posição | Modelo | Janeiro | Fevereiro |
|---------|--------|---------|-----------|
| 1º | VW T-Cross | 5.741 | 5.667 |
| 2º | VW Tera | 4.992 | 5.338 |
| 3º | Hyundai Creta | 4.428 | 5.045 |
| 4º | Jeep Compass | 4.503 | 4.169 |
| 5º | Chevrolet Tracker | 4.532 | 4.003 |
| 6º | Fiat Fastback | 3.927 | 3.833 |
| 7º | BYD Song | 3.802 | 3.702 |
| 8º | VW Nivus | 3.167 | 3.851 |
| 9º | Fiat Pulse | 3.193 | 3.057 |
| 10º | Nissan Kicks | 3.058 | 2.875 |

**Total geral: 40 modelos cadastrados — fonte Fenabrave Ed. 278**