# ⚡ Energy Analytics API

API REST para gestão e análise de consumo de energia, com autenticação JWT, arquitetura em camadas, testes automatizados, dashboard analítico e ambiente containerizado pronto para produção.

O sistema permite:

- registrar consumos mensais de clientes
- calcular métricas analíticas
- detectar anomalias de consumo
- visualizar dados em um dashboard interativo

Tudo protegido por autenticação segura baseada em token JWT.

---

# 🎯 Objetivo

Simular um backend profissional para monitoramento de consumo energético aplicando:

- Arquitetura limpa e modular
- Service Layer Pattern
- Separação de responsabilidades
- Segurança com JWT
- Testes automatizados
- Versionamento de API
- Containerização com Docker
- Dashboard analítico integrado

Projeto estruturado para futura integração com:

- dashboards corporativos
- ferramentas de BI
- aplicações frontend SPA (React, Vue, etc)

---

# 🚀 Tecnologias Utilizadas

Backend
- Python 3.11
- Django 5+
- Django REST Framework
- SimpleJWT

Banco de Dados
- PostgreSQL

Testes
- Pytest
- Pytest-Django

Infraestrutura
- Docker
- Docker Compose
- Gunicorn

Frontend
- Django Templates
- JavaScript
- Chart.js

Configuração
- Variáveis de ambiente (.env)

---

# 🏗 Estrutura do Projeto

energy-analytics-api/

apps/
- consumption/
  - models.py
  - serializers.py
  - views.py
  - selectors.py

- analytics/
  - services.py
  - views.py
  - urls.py

- users/

config/
- templates/
  - dashboard.html
  - anomalias.html
  - clientes.html
  - top_consumidores.html

- settings.py
- urls.py
- views.py

static/
- js/
  - dashboard.js
  - anomalias.js

Dockerfile  
docker-compose.yml  
requirements.txt  
README.md  

---

# 🧠 Arquitetura Aplicada

O projeto segue arquitetura em camadas:

models.py → Estrutura de dados  
serializers.py → Validação e transformação  
views.py → Camada HTTP (API)  
selectors.py → Consultas ao banco  
services.py → Regras de negócio  

## Benefícios

- Código desacoplado
- Melhor testabilidade
- Escalabilidade
- Clareza estrutural
- Padrão enterprise-ready

---

# 🔐 Autenticação JWT

A API utiliza autenticação stateless baseada em JWT.

## Obter Token

POST  
/api/token/

Body

{
  "username": "admin",
  "password": "sua_senha"
}

Resposta

{
  "refresh": "token_refresh",
  "access": "token_access"
}

## Usar Token

Authorization: Bearer SEU_ACCESS_TOKEN

---

# 📦 Versionamento da API

A API está versionada sob:

/api/v1/

Isso permite evolução futura sem quebrar compatibilidade.

---

# 📊 Endpoints Principais

## 👤 Clientes

Criar cliente  
POST /api/v1/clientes/

{
  "nome": "João Silva",
  "documento": "12345678900"
}

Listar clientes  
GET /api/v1/clientes/

---

## ⚡ Consumos

Criar consumo  
POST /api/v1/consumos/

{
  "cliente": 1,
  "mes": "2026-02-01",
  "consumo_kwh": 350.50
}

Listar consumos  
GET /api/v1/consumos/

---

# 📈 Analytics

O módulo analytics fornece métricas e insights sobre consumo energético.

## 📊 Resumo Geral

GET  
/api/v1/analytics/resumo-geral/

Retorna:

- total de consumo
- média geral
- total de clientes

---

## 📈 Crescimento Mensal

GET  
/api/v1/analytics/crescimento/?cliente_id=1

Retorna dados para gráfico de evolução de consumo.

---

## 📉 Crescimento Percentual

GET  
/api/v1/analytics/crescimento-percentual/?cliente_id=1

Calcula o crescimento do consumo em relação ao mês anterior.

---

## 🚨 Detecção de Anomalias

GET  
/api/v1/analytics/anomalias/

Detecta consumos anormais com base na média geral.

---

## 🏆 Top Consumidores

GET  
/api/v1/analytics/top-consumers/

Retorna ranking dos clientes com maior consumo.

---

## 📊 Média de Consumo por Cliente

GET  
/api/v1/analytics/media-consumo/?cliente_id=1

Exemplo de resposta

{
  "cliente_id": 1,
  "media": 325.25,
  "ultimo_consumo": 350.5
}

---

# 🖥 Dashboard Interativo

O projeto inclui um dashboard visual acessível em:

/dashboard/

Funcionalidades:

- métricas gerais de consumo
- gráfico de consumo mensal
- filtro por cliente
- crescimento percentual
- navegação para ranking de consumo
- visualização de anomalias

Tecnologias utilizadas:

- JavaScript
- Chart.js
- Django Templates

---

# 🚨 Página de Anomalias

Disponível em:

/anomalias/

Mostra consumos acima de um limite calculado automaticamente.

---

# 🧪 Testes Automatizados

O projeto utiliza:

- Pytest
- Pytest-Django
- Banco SQLite em memória para testes

Cobertura inclui:

- autenticação JWT
- acesso protegido a endpoints
- validação de permissões

Executar testes:

pytest

---

# ❤️ Health Check

Endpoint de verificação de status da aplicação

GET /health/

Retorna status da aplicação e conexão com banco.

---

# 🐳 Executando com Docker

## 1 Criar arquivo .env

DB_NAME=energy_analytics  
DB_USER=postgres  
DB_PASSWORD=1234  
DB_HOST=db  
DB_PORT=5432  
DEBUG=True  

O arquivo .env não deve ser versionado.

---

## 2 Subir os containers

docker compose up --build

---

## 3 Rodar migrations

docker compose exec web python manage.py migrate

---

## 4 Criar superuser

docker compose exec web python manage.py createsuperuser

---

## 5 Acessar aplicação

Admin  
http://localhost:8000/admin

Aplicação  
http://localhost:8000/

Dashboard  
http://localhost:8000/dashboard/

---

# ⚙️ Execução Local (Sem Docker)

git clone <url-do-repositorio>  

cd energy-analytics-api  

python -m venv venv  

venv\Scripts\activate  

pip install -r requirements.txt  

python manage.py migrate  

python manage.py runserver  

---

# 📈 Próximos Passos

- CI/CD pipeline
- Deploy automatizado
- Monitoramento e logs estruturados
- Rate limiting
- Cache com Redis
- Detecção avançada de anomalias
- Exportação de relatórios
- Integração com ferramentas de BI

---

# 👨‍💻 Autor

Lussandro Farias

Projeto desenvolvido para prática avançada de arquitetura backend com Django, APIs seguras, análise de dados e organização enterprise-ready.