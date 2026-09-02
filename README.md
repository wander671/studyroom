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

### Fase atual — Integração Flask + PostgreSQL

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

## 🎯 Próximos passos

O sistema de cadastro está completo: o formulário captura os dados, 
valida se as senhas conferem, gera um hash seguro com `werkzeug.security` 
e salva o novo usuário no banco `studyroom_db`.

O próximo passo é desenvolver o **sistema de login**, validando 
o e-mail e a senha digitados contra os dados salvos no banco 
(usando `check_password_hash` para comparar com o hash salvo).


Usuário
   │
   ▼
Formulário de Cadastro
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

O sistema deverá permitir o cadastro de novos usuários no banco de dados `studyroom_db`.

Após o cadastro, serão desenvolvidos:

1. 🔐 Sistema de login
2. 🔒 Autenticação e segurança
3. 🏠 Sistema de salas virtuais
4. 💬 Chat em tempo real
5. 🧑‍💻 Sistema de personagens
6. 🎵 Player de música
7. ⏱️ Pomodoro
8. 📊 Registro das sessões de estudo
9. 🧪 Testes
10. ☁️ Deploy

---

## 👨‍💻 Desenvolvedor

**Wander Farias**

Projeto desenvolvido para estudos, evolução profissional e construção de portfólio.

---

⭐ **StudyRoom está em desenvolvimento.**

Novas funcionalidades serão adicionadas durante as próximas etapas do projeto.

