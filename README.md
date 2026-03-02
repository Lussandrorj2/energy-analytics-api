# ⚡ Energy Analytics API

API REST para gestão e análise de consumo de energia, com autenticação JWT, arquitetura em camadas, testes automatizados e ambiente containerizado pronto para produção.

O sistema permite registrar consumos mensais de clientes, calcular métricas analíticas e proteger o acesso aos dados com autenticação segura baseada em token.

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
- Configuração para produção com Gunicorn

Projeto estruturado para futura integração com dashboards, ferramentas de BI ou frontend SPA.

---

# 🚀 Tecnologias Utilizadas

- Python 3.11
- Django 5+
- Django REST Framework
- SimpleJWT
- PostgreSQL
- Pytest + Pytest-Django
- Gunicorn
- Docker + Docker Compose
- Variáveis de ambiente (.env)

---

# 🏗 Estrutura do Projeto

energy-analytics-api/
│
├── apps/
│   ├── consumption/
│   ├── analytics/
│   └── users/
│
├── config/
│   ├── templates/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---

# 🧠 Arquitetura Aplicada

O projeto segue arquitetura em camadas:

- models.py → Estrutura de dados
- serializers.py → Validação e transformação
- views.py → Camada HTTP
- selectors.py → Consultas ao banco
- services.py → Regras de negócio

## Benefícios

- Melhor testabilidade
- Código desacoplado
- Escalabilidade
- Clareza estrutural
- Padrão enterprise-ready

---

# 🔐 Autenticação JWT

A API utiliza autenticação stateless baseada em JWT.

## Obter Token

POST  
/api/token/

Body:

{
  "username": "admin",
  "password": "sua_senha"
}

Resposta:

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

## 📈 Analytics

Média de consumo por cliente:

GET  
/api/v1/analytics/media-consumo/?cliente_id=1

Exemplo de resposta:

{
  "cliente_id": 1,
  "media": 325.25,
  "ultimo_consumo": 350.5
}

---

# 🖥 Interface HTML

O projeto também inclui páginas renderizadas via Django Templates:

- /
- /dashboard/
- /clientes-view/
- /analytics-view/
- /consumo/

Essas páginas simulam uma camada frontend simples integrada à API.

---

# 🧪 Testes Automatizados

O projeto utiliza:

- Pytest
- Pytest-Django
- Banco SQLite em memória para testes

Cobertura inclui:

- Autenticação JWT
- Acesso protegido a endpoints
- Validação de permissões

Executar testes:

pytest

---

# ❤️ Health Check

Endpoint de verificação de status da aplicação:

GET /health/

Retorna status da aplicação e conexão com banco.

---

# 🐳 Executando com Docker (Produção Ready)

## 1️⃣ Criar arquivo .env

DB_NAME=energy_analytics  
DB_USER=postgres  
DB_PASSWORD=1234  
DB_HOST=db  
DB_PORT=5432  
DEBUG=True  

⚠️ O arquivo .env não deve ser versionado.

---

## 2️⃣ Subir os containers

docker compose up --build

---

## 3️⃣ Rodar migrations

docker compose exec web python manage.py migrate

---

## 4️⃣ Criar superuser

docker compose exec web python manage.py createsuperuser

---

## 5️⃣ Acessar aplicação

Admin:
http://localhost:8000/admin

Aplicação:
http://localhost:8000/

---

# 🏭 Produção

A aplicação roda com:

- Gunicorn como servidor WSGI
- Configuração via variáveis de ambiente
- Coleta de arquivos estáticos (collectstatic)
- PostgreSQL como banco padrão

Pronta para deploy em:

- Render
- Railway
- AWS
- DigitalOcean
- VPS Linux

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
- Detecção de anomalias de consumo

---

# 👨‍💻 Autor

Lussandro Farias

Projeto desenvolvido para prática avançada de arquitetura backend com Django, APIs seguras e organização enterprise-ready.
