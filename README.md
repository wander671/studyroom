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

- 👤 Cadastro e login de usuários
- 🧑‍💻 Escolha de personagem/avatar
- 🏠 Salas virtuais de estudo
- 👥 Usuários online
- 💬 Chat em tempo real
- ⚡ Comunicação através de WebSockets
- 🎵 Música ambiente
- ⏱️ Cronômetro Pomodoro
- 📊 Registro de sessões de estudo
- 🔐 Autenticação e segurança
- 📱 Interface responsiva
- 🌐 API REST
- ☁️ Deploy da aplicação

---

## 🛠️ Tecnologias

### Backend

- 🐍 Python
- 🌐 Flask
- ⚡ Flask-SocketIO
- 🗄️ PostgreSQL

### Frontend

- HTML5
- CSS3
- JavaScript

### Ferramentas

- Git
- GitHub
- VS Code
- Pytest

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


📁 Estrutura inicial
Sala de Estudos Virtual/
│
├── .venv/
│
├── app/
│
├── static/
│   ├── css/
│   ├── imagens/
│   ├── js/
│   └── music/
│
├── templates/
│
├── tests/
│
├── ARQUITETURA.MD
├── ARQUITETURA(projeto).MD
├── requirements.txt
└── run.py
📌 Status do projeto
Fase atual

Aula 1 — Configuração inicial

 Planejamento do projeto
 Definição da arquitetura inicial
 Criação do ambiente virtual
 Configuração do Flask
 Criação da estrutura inicial
 Primeiro teste do servidor Flask
 Configuração do PostgreSQL
 Sistema de usuários
 Sistema de salas
 Chat em tempo real
 Sistema de personagens
 Player de música
 Pomodoro
 Testes
 Deploy
🎯 Próximos passos

O próximo objetivo será estruturar a aplicação Flask utilizando uma arquitetura mais organizada, preparando o projeto para receber o banco de dados PostgreSQL e os demais recursos.

👨‍💻 Desenvolvedor

Wander Farias

Projeto desenvolvido para estudos e construção de portfólio profissional.

⭐ Projeto em desenvolvimento. Novas funcionalidades serão adicionadas durante as próximas etapas.