# ⚡ Energy Analytics API

API REST para **gestão e análise de consumo de energia**, construída com **Django REST Framework**, arquitetura modular em camadas e ambiente **containerizado com Docker**, pronta para uso em produção.

O sistema permite:

* registrar consumos energéticos mensais de clientes
* calcular métricas analíticas
* detectar anomalias de consumo
* visualizar dados em um dashboard interativo
* analisar padrões de consumo energético

A aplicação inclui **API versionada, autenticação JWT, arquitetura enterprise-ready e dashboard analítico integrado**.

---

# 🎯 Objetivo do Projeto

Este projeto simula um **backend profissional de monitoramento energético**, aplicando boas práticas modernas de desenvolvimento backend.

Principais conceitos aplicados:

* Arquitetura limpa e modular
* Service Layer Pattern
* Separação clara de responsabilidades
* Segurança com autenticação JWT
* Versionamento de API
* Testes automatizados
* Containerização com Docker
* Dashboard analítico integrado

A estrutura foi projetada para futura integração com:

* dashboards corporativos
* ferramentas de Business Intelligence
* aplicações frontend SPA (React, Vue, Angular)
* sistemas de monitoramento energético

---

# 🚀 Tecnologias Utilizadas

## Backend

* Python 3.11
* Django 5+
* Django REST Framework
* SimpleJWT (Autenticação)

## Banco de Dados

* PostgreSQL

## Testes

* Pytest
* Pytest-Django

## Infraestrutura

* Docker
* Docker Compose
* Gunicorn

## Frontend (Dashboard)

* Django Templates
* JavaScript
* Chart.js

## Configuração

* Variáveis de ambiente (.env)

---

# 🏗 Estrutura do Projeto

```
energy-analytics-api/

apps/
 ├── analytics/
 │   ├── services.py
 │   ├── views.py
 │   └── urls.py
 │
 ├── consumption/
 │   ├── models.py
 │   ├── serializers.py
 │   ├── selectors.py
 │   └── views.py
 │
 └── users/
     ├── models.py
     ├── serializers.py
     └── views.py

config/
 ├── templates/
 │   ├── dashboard.html
 │   ├── anomalias.html
 │   ├── clientes.html
 │   └── top_consumidores.html
 │
 ├── settings.py
 ├── urls.py
 └── views.py

static/
 └── js/
     ├── dashboard.js
     └── anomalias.js

Dockerfile  
docker-compose.yml  
requirements.txt  
README.md
```

---

# 🧠 Arquitetura Aplicada

O projeto utiliza **arquitetura em camadas**, comum em sistemas enterprise.

```
models.py → Estrutura de dados
serializers.py → Validação e transformação
views.py → Camada HTTP (API)
selectors.py → Consultas ao banco
services.py → Regras de negócio
```

### Benefícios

* Código desacoplado
* Melhor testabilidade
* Escalabilidade
* Clareza estrutural
* Fácil manutenção
* Arquitetura enterprise-ready

---

# 🔐 Autenticação JWT

A API utiliza autenticação **stateless baseada em JSON Web Token**.

## Obter Token

POST

```
/api/token/
```

Body

```
{
  "username": "admin",
  "password": "sua_senha"
}
```

Resposta

```
{
  "refresh": "token_refresh",
  "access": "token_access"
}
```

## Usar Token nas requisições

```
Authorization: Bearer SEU_ACCESS_TOKEN
```

---

# 📦 Versionamento da API

Todas as rotas da API são versionadas:

```
/api/v1/
```

Isso permite evolução da API sem quebrar compatibilidade com versões anteriores.

---

# 📊 Endpoints Principais

## 👤 Clientes

Criar cliente

POST

```
/api/v1/clientes/
```

Body

```
{
  "nome": "João Silva",
  "documento": "12345678900"
}
```

Listar clientes

```
GET /api/v1/clientes/
```

---

## ⚡ Consumos

Criar consumo

POST

```
/api/v1/consumos/
```

```
{
  "cliente": 1,
  "mes": "2026-02-01",
  "consumo_kwh": 350.50
}
```

Listar consumos

```
GET /api/v1/consumos/
```

---

# 📈 Analytics

O módulo **analytics** fornece métricas e insights sobre consumo energético.

---

## 📊 Resumo Geral

```
GET /api/v1/analytics/resumo-geral/
```

Retorna:

* total de consumo
* média geral
* total de clientes

---

## 📈 Crescimento Mensal

```
GET /api/v1/analytics/crescimento/?cliente_id=1
```

Retorna dados para gráfico de evolução de consumo.

---

## 📉 Crescimento Percentual

```
GET /api/v1/analytics/crescimento-percentual/?cliente_id=1
```

Calcula o crescimento em relação ao mês anterior.

---

## 🚨 Detecção de Anomalias

```
GET /api/v1/analytics/anomalias/
```

Detecta consumos anormais com base na média geral.

---

## 🏆 Top Consumidores

```
GET /api/v1/analytics/top-consumers/
```

Retorna ranking dos clientes com maior consumo.

---

## 📊 Média de Consumo por Cliente

```
GET /api/v1/analytics/media-consumo/?cliente_id=1
```

Exemplo de resposta:

```
{
  "cliente_id": 1,
  "media": 325.25,
  "ultimo_consumo": 350.5
}
```

---

# 🖥 Dashboard Interativo

O projeto inclui um **dashboard visual integrado**, acessível em:

```
/dashboard/
```

Funcionalidades:

* métricas gerais de consumo
* gráfico de consumo mensal
* filtro por cliente
* crescimento percentual
* ranking de consumo
* visualização de anomalias

Tecnologias utilizadas:

* Chart.js
* JavaScript
* Django Templates

---

# 🚨 Página de Anomalias

Disponível em:

```
/anomalias/
```

Mostra consumos acima de um limite calculado automaticamente.

---

# 🧪 Testes Automatizados

O projeto utiliza:

* Pytest
* Pytest-Django

Cobertura inclui:

* autenticação JWT
* acesso protegido a endpoints
* validação de permissões

Executar testes:

```
pytest
```

---

# ❤️ Health Check

Endpoint de verificação da aplicação.

```
GET /health/
```

Retorna o status da aplicação e conexão com banco de dados.

---

# 🐳 Executando com Docker

## 1 Criar arquivo `.env`

```
DB_NAME=energy_analytics
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=db
DB_PORT=5432
DEBUG=True
```

O arquivo `.env` **não deve ser versionado**.

---

## 2 Subir containers

```
docker compose up --build
```

---

## 3 Rodar migrations

```
docker compose exec web python manage.py migrate
```

---

## 4 Criar superuser

```
docker compose exec web python manage.py createsuperuser
```

---

## 5 Acessar aplicação

Admin

```
http://localhost:8000/admin
```

Aplicação

```
http://localhost:8000/
```

Dashboard

```
http://localhost:8000/dashboard/
```

---

# ⚙️ Execução Local (Sem Docker)

```
git clone <url-do-repositorio>

cd energy-analytics-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

# 📈 Melhorias Futuras

* CI/CD pipeline
* Deploy automatizado
* Monitoramento e logs estruturados
* Cache com Redis
* Rate limiting
* Detecção avançada de anomalias
* Exportação de relatórios
* Integração com ferramentas de BI
* Dashboard em React

---

# 👨‍💻 Autor

**Lussandro Farias**

Projeto desenvolvido para prática avançada de:

* arquitetura backend
* APIs REST seguras
* análise de dados
* organização enterprise-ready
* boas práticas com Django e Docker
