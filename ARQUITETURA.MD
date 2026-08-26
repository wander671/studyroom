📚 AULA 1 — Planejamento e Arquitetura

Nesta primeira aula ainda não vamos sair programando. Primeiro vamos deixar o projeto bem definido. Isso vai evitar aquela bagunça de começar a criar arquivos e depois não saber onde cada coisa deve ficar.

🎯 1. Objetivo do projeto

Nossa aplicação permitirá que uma pessoa:

Crie uma conta.
Faça login.
Escolha um personagem.
Escolha uma sala de estudos.
Entre na sala.
Veja outras pessoas estudando.
Converse pelo chat em tempo real.
Escute música.
Utilize um cronômetro Pomodoro.
Saia da sala.

A ideia principal é:

Criar uma experiência de estudo compartilhado para diminuir a sensação de estudar sozinho.

🏗️ 2. Como o sistema vai funcionar

Vamos pensar no caminho do usuário:

                    INÍCIO
                       │
                       ▼
                  ┌─────────┐
                  │ Cadastro│
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │  Login  │
                  └────┬────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Escolher Avatar │
              └────────┬────────┘
                       │
                       ▼
                ┌─────────────┐
                │ Lista Salas │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ Sala Virtual│
                └──────┬──────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       💬 Chat       🎵 Música    ⏱️ Foco
          │            │            │
          └────────────┼────────────┘
                       ▼
                  👥 Usuários
                    Online

Esse fluxo será a base do projeto.

🧩 3. MVP — nossa primeira versão

Para não transformar o projeto em algo gigantesco, vamos definir o MVP.

MVP = Minimum Viable Product, ou Produto Mínimo Viável.

Nossa primeira versão terá:

👤 Usuários
Cadastro
Login
Logout
Avatar
🏠 Salas
Lista de salas
Entrar na sala
Sair da sala
Ver participantes
💬 Comunicação
Chat em tempo real
Mensagens
Usuários online
Entrada/saída de usuários
🎵 Ambiente
Música
Player
Controle de volume
⏱️ Estudos
Pomodoro
Contador de foco
Pausa
🐍 4. Tecnologias

Nossa stack inicial fica:

Tecnologia	Função
Python	Backend
Flask	Framework web
PostgreSQL	Banco de dados
Flask-SocketIO	Comunicação em tempo real
HTML5	Estrutura
CSS3	Interface
JavaScript	Interações em tempo real
Git	Versionamento
GitHub	Repositório
Pytest	Testes
Deploy	Publicação