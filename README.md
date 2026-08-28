# 📚 StudyRoom — Sala de Estudos Virtual

> **Estude junto. Não estude sozinho.**

O **StudyRoom** é uma plataforma de estudos colaborativos criada para proporcionar uma experiência mais interativa para pessoas que estudam sozinhas.

A proposta é permitir que usuários entrem em salas virtuais de estudo, escolham um personagem, encontrem outras pessoas estudando no mesmo ambiente, conversem através de um chat em tempo real, escutem música e utilizem ferramentas para melhorar a concentração.

🚧 **Projeto em desenvolvimento**

---

## 🎯 Objetivo

Criar uma experiência de estudo compartilhado, proporcionando a sensação de estar estudando junto com outras pessoas, mesmo que cada usuário esteja em seu próprio ambiente.

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
├── senha
└── data_criacao
```

A tabela `usuarios` já foi criada e testada no PostgreSQL.

Também foi realizado um cadastro de usuário para validar o funcionamento do banco.

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

### Fase atual — Integração com PostgreSQL

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
* [ ] Integração do banco com o Flask
* [ ] Sistema de cadastro
* [ ] Sistema de login
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

O próximo objetivo será integrar a conexão PostgreSQL ao Flask.

A partir dessa etapa, o StudyRoom começará a trabalhar com dados reais através da aplicação:

```text
Usuário
   │
   ▼
Formulário
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

O primeiro recurso será a criação do **sistema de cadastro de usuários**, seguido pelo sistema de login e autenticação.

---

## 👨‍💻 Desenvolvedor

**Wander Farias**

Projeto desenvolvido para estudos, evolução profissional e construção de portfólio.

---

⭐ **StudyRoom está em desenvolvimento.**

Novas funcionalidades serão adicionadas durante as próximas etapas do projeto.
