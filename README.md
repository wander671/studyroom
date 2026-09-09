# 📚 StudyRoom — Sala de Estudos Virtual

> **Estude junto. Não estude sozinho.**

O **StudyRoom** é uma plataforma de estudos colaborativos criada para proporcionar uma experiência mais interativa para pessoas que estudam sozinhas.

A proposta é permitir que usuários entrem em salas virtuais de estudo, escolham um personagem, encontrem outras pessoas estudando no mesmo ambiente, conversem através de um chat em tempo real, escutem música e utilizem ferramentas para melhorar a concentração.

Além disso, o StudyRoom está evoluindo para se tornar também uma **plataforma de aprendizagem para quem está começando em tecnologia**, com trilhas de estudo organizadas (cursos, módulos e aulas em vídeo), permitindo que o usuário siga um caminho estruturado de aprendizado, além de estudar em comunidade.

🚧 **Projeto em desenvolvimento**

---

## 🎯 Objetivo

Criar uma experiência de estudo compartilhado, proporcionando a sensação de estar estudando junto com outras pessoas, mesmo que cada usuário esteja em seu próprio ambiente — combinando isso com trilhas de aprendizagem estruturadas para iniciantes em tecnologia.

---

## 🚀 Funcionalidades planejadas

* 👤 Cadastro e login de usuários
* 🧑‍💻 Escolha de personagem/avatar
* 🏠 Salas virtuais de estudo
* 👥 Usuários online
* 💬 Chat em tempo real
* ⚡ Comunicação através de WebSockets
* 🎵 Música ambiente
* ⏱️ Cronômetro Pomodoro
* 📊 Registro de sessões de estudo
* 🔐 Autenticação e segurança
* 📱 Interface responsiva
* 🌐 API REST
* 🎓 Trilhas de aprendizagem (cursos, módulos e aulas em vídeo)
* 📈 Registro de progresso do usuário nas trilhas
* ☁️ Deploy da aplicação

---

## 🛠️ Tecnologias

### Backend

* 🐍 Python
* 🌐 Flask
* ⚡ Flask-SocketIO
* 🐘 PostgreSQL
* 🔌 Psycopg
* 🔐 Python-dotenv
* 🔒 Werkzeug Security (hash de senha)

### Frontend

* HTML5
* CSS3
* JavaScript

### Ferramentas

* Git
* GitHub
* VS Code
* pgAdmin 4
* Pytest

---

## 🗄️ Banco de Dados

O projeto utiliza **PostgreSQL 18** como banco de dados principal.

Banco utilizado:

```text
studyroom_db
```

### Tabela atual

```text
usuarios
│
├── id
├── nome
├── email
├── senha (hash)
└── data_criacao
```

A tabela `usuarios` já foi criada e testada no PostgreSQL, com cadastro e login de usuários reais validados.

> 🔐 As credenciais do banco são armazenadas através de variáveis de ambiente utilizando o arquivo `.env`. O arquivo `.env` não deve ser enviado para o GitHub.

---

## 🔌 Conexão Python → PostgreSQL

A comunicação entre o Python e o PostgreSQL é realizada utilizando **Psycopg**.

O arquivo `database.py` centraliza a conexão com o banco de dados.

```text
Python
   │
   ▼
database.py
   │
   ▼
python-dotenv
   │
   ▼
Psycopg
   │
   ▼
PostgreSQL 18
   │
   ▼
studyroom_db
```

A conexão foi testada com sucesso através de um script de teste.

```text
CONEXÃO REALIZADA COM SUCESSO! ✅
StudyRoom conectado ao PostgreSQL! 📚🐘
```

---

## 🌐 Integração Flask → PostgreSQL

A conexão com o PostgreSQL foi integrada à aplicação Flask.

A rota:

```text
/teste-banco
```

é utilizada para validar a comunicação entre o Flask e o banco de dados PostgreSQL.

Fluxo da aplicação:

```text
Navegador
   │
   ▼
Flask
   │
   ▼
/teste-banco
   │
   ▼
conectar_banco()
   │
   ▼
database.py
   │
   ▼
Psycopg
   │
   ▼
PostgreSQL 18
```

Quando a conexão é realizada com sucesso, a aplicação retorna:

```text
StudyRoom conectado ao PostgreSQL! 🐘
```

A rota também possui **tratamento de erros**, utilizando `try/except`, permitindo identificar falhas na conexão e retornar uma resposta HTTP `500` quando ocorre um erro interno.

Essa etapa confirma a integração entre o **Flask**, o módulo `database.py` e o **PostgreSQL**.

---

## 🔐 Cadastro e Login de Usuários

O fluxo completo de autenticação já está implementado:

**Cadastro (`/cadastro`)**
- Captura `nome`, `email`, `senha` e `confirmar_senha` via `request.form`
- Valida se a senha e a confirmação de senha são iguais
- Gera um hash seguro da senha com `generate_password_hash` (Werkzeug) — a senha original nunca é salva no banco
- Insere o novo usuário no PostgreSQL com uma query parametrizada (`%s`), evitando SQL Injection

**Login (`/login`)**
- Captura `email` e `senha` via `request.form`
- Busca o usuário no banco pelo `email`
- Compara a senha digitada com o hash salvo usando `check_password_hash`
- Utiliza **mensagens de erro genéricas** ("E-mail ou senha incorretos") tanto para email inexistente quanto para senha errada, evitando enumeração de usuários (prática de segurança conhecida)

**Feedback ao usuário**
- Mensagens de erro e sucesso são exibidas através do sistema `flash()` do Flask, com uma `SECRET_KEY` protegida via `.env`

---

## 🏗️ Arquitetura

A aplicação será construída utilizando uma arquitetura organizada, separando responsabilidades entre backend, frontend, banco de dados e comunicação em tempo real.

```text
                    ┌─────────────────┐
                    │    FRONTEND     │
                    │  HTML/CSS/JS    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FLASK       │
                    │     PYTHON      │
                    └───────┬─┬───────┘
                            │ │
                 ┌──────────┘ └──────────┐
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │   PostgreSQL    │     │  Flask-SocketIO │
        │    Database     │     │  Tempo Real     │
        └─────────────────┘     └─────────────────┘
```

---

## 📁 Estrutura atual

```text
Sala de Estudos Virtual/
│
├── .venv/
│
├── .env
├── .gitignore
├── database.py
├── run.py
├── requirements.txt
│
├── static/
│   ├── css/
│   ├── images/
│   │   └── foto_perfil.jpg
│   ├── js/
│   └── music/
│
├── templates/
│
├── tests/
│
├── ARQUITETURA.MD
└── ARQUITETURA(projeto).MD
```

> 🔐 O arquivo `.env` contém informações sensíveis e está protegido pelo `.gitignore`.

---

## 📌 Status do projeto

### Fase atual — Autenticação completa (cadastro + login)

* [x] Planejamento do projeto
* [x] Definição da arquitetura inicial
* [x] Criação do ambiente virtual
* [x] Configuração do Flask
* [x] Criação da estrutura inicial
* [x] Primeiro teste do servidor Flask
* [x] Criação da identidade visual do projeto
* [x] Inclusão da foto do desenvolvedor na Home
* [x] Instalação e configuração do PostgreSQL
* [x] Criação do banco `studyroom_db`
* [x] Criação da tabela `usuarios`
* [x] Inserção de usuário de teste
* [x] Instalação do Psycopg
* [x] Instalação do Python-dotenv
* [x] Configuração do arquivo `.env`
* [x] Proteção do `.env` através do `.gitignore`
* [x] Criação do `database.py`
* [x] Teste de conexão Python → PostgreSQL
* [x] Integração do banco com o Flask
* [x] Criação da rota `/teste-banco`
* [x] Tratamento de erros na conexão com o banco
* [x] Criação do formulário de cadastro (HTML)
* [x] Rota `/cadastro` configurada para aceitar GET e POST
* [x] Captura dos dados do formulário com `request.form`
* [x] Validação de senha e confirmação de senha
* [x] Mensagens de erro com `flash()`
* [x] Configuração da `SECRET_KEY` via `.env`
* [x] Hash de senha com `werkzeug.security` (generate_password_hash)
* [x] Sistema de cadastro salvando usuário no PostgreSQL
* [x] Sistema de login validando email e senha
* [x] Busca de usuário no banco por email (SELECT)
* [x] Comparação de senha com `check_password_hash`
* [x] Mensagens de erro/sucesso no login (flash)
* [x] Tratamento de erro genérico por segurança (evita enumeração de usuários)
* [ ] Sessão de usuário logado (Flask session)
* [ ] Modelagem das trilhas de aprendizagem
* [ ] Sistema de salas
* [ ] Chat em tempo real
* [ ] Sistema de personagens
* [ ] Player de música
* [ ] Pomodoro
* [ ] Registro de sessões
* [ ] Testes
* [ ] Deploy

---

## 🎯 Próximos passos

Cadastro e login estão completos e funcionais, com senhas protegidas por hash e mensagens de feedback para o usuário via `flash()`.

O próximo passo é implementar **sessão de usuário** (Flask `session`), para que o sistema "lembre" que o usuário está autenticado ao navegar entre páginas.

Depois disso, o projeto vai seguir por duas frentes:

1. 🎓 **Trilhas de aprendizagem** — modelagem de `trilhas`, `modulos` e `aulas` (com vídeos do YouTube), permitindo que o usuário siga um caminho estruturado de estudo com registro de progresso
2. 🏠 **Salas virtuais e chat em tempo real** — funcionalidade social original do projeto, usando Flask-SocketIO

Fluxo atual de autenticação:

```text
Usuário
   │
   ▼
Formulário de Cadastro/Login
   │
   ▼
Flask
   │
   ▼
database.py
   │
   ▼
PostgreSQL
   │
   ▼
usuarios
```

Ordem geral de desenvolvimento planejada:

1. ✅ Sistema de cadastro
2. ✅ Sistema de login
3. 🔒 Sessão de usuário autenticado
4. 🎓 Trilhas de aprendizagem
5. 🏠 Sistema de salas virtuais
6. 💬 Chat em tempo real
7. 🧑‍💻 Sistema de personagens
8. 🎵 Player de música
9. ⏱️ Pomodoro
10. 📊 Registro das sessões de estudo
11. 🧪 Testes
12. ☁️ Deploy

---

## 👨‍💻 Desenvolvedor

**Wander Farias**

Projeto desenvolvido para estudos, evolução profissional e construção de portfólio.

---

⭐ **StudyRoom está em desenvolvimento.**

Novas funcionalidades serão adicionadas durante as próximas etapas do projeto.