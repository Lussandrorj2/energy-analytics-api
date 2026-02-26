# ⚡ Energy Analytics API

API backend para gerenciamento e análise de consumo energético, desenvolvida com Django e Django REST Framework.

O projeto demonstra:

- Arquitetura modular
- Separação de responsabilidades (Service Layer Pattern)
- Autenticação JWT
- Organização escalável de rotas
- Estrutura preparada para crescimento

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 5+
- Django REST Framework
- SimpleJWT (Autenticação JWT)
- SQLite (ambiente de desenvolvimento)

---

## 🏗 Estrutura do Projeto

energy-analytics-api/
│
├── apps/
│   ├── consumption/
│   ├── analytics/
│   └── users/
│
├── config/
├── manage.py
└── README.md

### Organização Interna

O projeto segue separação de responsabilidades:

- models.py → Estrutura de dados
- serializers.py → Transformação de dados
- views.py → Camada HTTP
- selectors.py → Consultas ao banco
- services.py → Regras de negócio

Essa abordagem facilita manutenção e escalabilidade.

---

## 🔐 Autenticação

A API utiliza autenticação JWT (JSON Web Token).

### Obter Token

POST  
/api/token/

Body:

{
  "username": "seu_usuario",
  "password": "sua_senha"
}

Resposta:

{
  "refresh": "token_refresh",
  "access": "token_access"
}

Para acessar endpoints protegidos:

Authorization: Bearer SEU_ACCESS_TOKEN

---

## 📊 Endpoints Principais

### Clientes

Criar cliente:
POST /api/v1/clientes/

Exemplo:

{
  "nome": "João Silva",
  "documento": "12345678900"
}

Listar clientes:
GET /api/v1/clientes/

---

### Consumos

Criar consumo:
POST /api/v1/consumos/

{
  "cliente": 1,
  "mes": "2026-02-01",
  "consumo_kwh": 350.50
}

Listar consumos:
GET /api/v1/consumos/

---

### Analytics

Média de consumo por cliente:

GET /api/v1/analytics/media-consumo/?cliente_id=1

Exemplo de resposta:

{
  "cliente_id": 1,
  "media": 325.25,
  "ultimo_consumo": 350.5
}

---

## ⚙️ Como Executar Localmente (Windows)

git clone <url-do-repositorio>
cd energy-analytics-api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

Acesse:
http://127.0.0.1:8000/

---

## 🧠 Decisões de Arquitetura

- Uso de ViewSets para CRUD
- JWT para autenticação stateless
- Service Layer para regras de negócio
- Selector Layer para consultas agregadas
- Estrutura modular por domínio

Essa organização permite evolução para:

- PostgreSQL
- Docker
- Versionamento de API
- Testes automatizados
- Deploy em produção

---

## 📈 Próximos Passos

- Versionamento da API (/api/v1/)
- Dockerização
- PostgreSQL
- Testes automatizados
- Documentação automática (Swagger)

---

## 👨‍💻 Autor
Lussandro Farias

Projeto desenvolvido para prática de arquitetura backend com Django.