# ⚡ Energy Analytics API

API REST para gestão e análise de consumo de energia.

O sistema permite registrar consumos mensais de clientes, calcular métricas analíticas e proteger o acesso aos dados por meio de autenticação JWT.  
O projeto demonstra boas práticas de arquitetura backend utilizando Django e Django REST Framework, com banco PostgreSQL e containerização via Docker.

---

## 🎯 Objetivo

Simular um sistema backend para monitoramento de consumo energético, aplicando:

- Arquitetura em camadas
- Separação de responsabilidades
- Segurança em APIs REST
- Organização modular e escalável
- Containerização e ambiente configurável

A API foi estruturada para permitir futura integração com dashboards, ferramentas de BI ou aplicações frontend.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 5+
- Django REST Framework
- SimpleJWT (Autenticação JWT)
- PostgreSQL
- Docker + Docker Compose
- Variáveis de ambiente (.env)

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
├── Dockerfile
├── docker-compose.yml
└── README.md

### Organização Interna

O projeto segue arquitetura em camadas:

- models.py → Estrutura de dados
- serializers.py → Transformação e validação de dados
- views.py → Camada HTTP
- selectors.py → Consultas ao banco
- services.py → Regras de negócio

Essa abordagem melhora:

- Manutenção
- Testabilidade
- Escalabilidade
- Clareza arquitetural

---

## 🔐 Autenticação

A API utiliza autenticação JWT (JSON Web Token), garantindo acesso seguro e stateless.

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

## 📦 Versionamento da API

A API está versionada sob o namespace:

/api/v1/

Isso permite evolução futura da API sem quebrar compatibilidade.

---

## 📊 Endpoints Principais

### 👤 Clientes

Criar cliente:  
POST /api/v1/clientes/

{
  "nome": "João Silva",
  "documento": "12345678900"
}

Listar clientes:  
GET /api/v1/clientes/

---

### ⚡ Consumos

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

### 📈 Analytics

Média de consumo por cliente:

GET  
/api/v1/analytics/media-consumo/?cliente_id=1

O endpoint analítico calcula:

- Média histórica de consumo por cliente
- Último consumo registrado
- Estrutura pronta para integração com dashboards

Exemplo de resposta:

{
  "cliente_id": 1,
  "media": 325.25,
  "ultimo_consumo": 350.5
}

---

## 🐳 Executando com Docker (Recomendado)

### 1️⃣ Criar arquivo .env

Na raiz do projeto, criar um arquivo chamado `.env` com:

DB_NAME=energy_analytics  
DB_USER=postgres  
DB_PASSWORD=1234  
DB_HOST=db  
DB_PORT=5432  

⚠️ O arquivo `.env` não deve ser versionado.

---

### 2️⃣ Subir os containers

docker compose up --build

---

### 3️⃣ Rodar as migrations

Em outro terminal:

docker compose exec web python manage.py migrate

---

### 4️⃣ Criar superuser

docker compose exec web python manage.py createsuperuser

---

### 5️⃣ Acessar aplicação

http://localhost:8000/admin

---

## ⚙️ Execução Local (Sem Docker)

git clone <url-do-repositorio>  
cd energy-analytics-api  

python -m venv venv  
venv\Scripts\activate  

pip install -r requirements.txt  

python manage.py migrate  
python manage.py runserver  

---

## 🧠 Decisões de Arquitetura

- Uso de ViewSets para CRUD automático
- Autenticação JWT para segurança stateless
- Service Layer Pattern (arquitetura em camadas)
- Selector Layer para consultas agregadas
- Estrutura modular organizada por domínio
- Versionamento de API (/api/v1/)
- PostgreSQL como banco padrão
- Configuração via variáveis de ambiente
- Containerização completa com Docker

Essa organização permite evolução futura para:

- Gunicorn (modo produção)
- Testes automatizados
- CI/CD
- Deploy em ambiente de produção
- Monitoramento e logs estruturados

---

## 📈 Próximos Passos

- Configuração com Gunicorn
- Implementação de testes automatizados
- Pipeline de CI/CD
- Deploy em nuvem (Render, Railway ou AWS)
- Implementação de detecção de anomalias de consumo

---

## 👨‍💻 Autor

Lussandro Farias

Projeto desenvolvido para prática avançada de arquitetura backend com Django e construção de APIs analíticas seguras.