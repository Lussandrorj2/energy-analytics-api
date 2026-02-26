# ⚡ Energy Analytics API

API REST para gestão e análise de consumo de energia.

O sistema permite registrar consumos mensais de clientes, calcular métricas analíticas e proteger o acesso aos dados por meio de autenticação JWT.  
O projeto demonstra boas práticas de arquitetura backend utilizando Django e Django REST Framework.

---

## 🎯 Objetivo

Simular um sistema backend para monitoramento de consumo energético, aplicando:

- Arquitetura em camadas
- Separação de responsabilidades
- Segurança em APIs REST
- Organização modular e escalável

A API foi estruturada para permitir futura integração com dashboards, ferramentas de BI ou aplicações frontend.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 5+
- Django REST Framework
- SimpleJWT (Autenticação JWT)
- SQLite (ambiente de desenvolvimento)

Preparado para futura migração para PostgreSQL.

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

O projeto segue arquitetura em camadas:

- `models.py` → Estrutura de dados
- `serializers.py` → Transformação e validação de dados
- `views.py` → Camada HTTP
- `selectors.py` → Consultas ao banco
- `services.py` → Regras de negócio

Essa abordagem melhora:

- Manutenção
- Testabilidade
- Escalabilidade
- Clareza arquitetural

---

## 🔐 Autenticação

A API utiliza autenticação JWT (JSON Web Token), garantindo acesso seguro e stateless.

### Obter Token

**POST**  
`/api/token/`

Body:

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Resposta:

```json
{
  "refresh": "token_refresh",
  "access": "token_access"
}
```

Para acessar endpoints protegidos:

```
Authorization: Bearer SEU_ACCESS_TOKEN
```

---

## 📊 Endpoints Principais

### 👤 Clientes

Criar cliente:  
**POST** `/api/v1/clientes/`

```json
{
  "nome": "João Silva",
  "documento": "12345678900"
}
```

Listar clientes:  
**GET** `/api/v1/clientes/`

---

### ⚡ Consumos

Criar consumo:  
**POST** `/api/v1/consumos/`

```json
{
  "cliente": 1,
  "mes": "2026-02-01",
  "consumo_kwh": 350.50
}
```

Listar consumos:  
**GET** `/api/v1/consumos/`

---

### 📈 Analytics

Média de consumo por cliente:

**GET**  
`/api/v1/analytics/media-consumo/?cliente_id=1`

O endpoint analítico calcula:

- Média histórica de consumo por cliente
- Último consumo registrado
- Estrutura pronta para integração com dashboards

Exemplo de resposta:

```json
{
  "cliente_id": 1,
  "media": 325.25,
  "ultimo_consumo": 350.5
}
```

---

## ⚙️ Como Executar Localmente (Windows)

```bash
git clone <url-do-repositorio>
cd energy-analytics-api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

---

## 🧠 Decisões de Arquitetura

- Uso de ViewSets para CRUD automático
- Autenticação JWT para segurança stateless
- Service Layer Pattern (arquitetura em camadas)
- Selector Layer para consultas agregadas
- Estrutura modular organizada por domínio
- Versionamento de API (`/api/v1/`)

Essa organização permite evolução futura para:

- PostgreSQL
- Docker
- Testes automatizados
- Documentação automática (Swagger/OpenAPI)
- Deploy em ambiente de produção

---

## 📈 Próximos Passos

- Dockerização
- Migração para PostgreSQL
- Implementação de testes automatizados
- Monitoramento e logs estruturados
- Implementação de detecção de anomalias de consumo

---

## 👨‍💻 Autor

**Lussandro Farias**

Projeto desenvolvido para prática avançada de arquitetura backend com Django e construção de APIs analíticas seguras.
