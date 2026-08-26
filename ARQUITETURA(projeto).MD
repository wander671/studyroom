📚 Projeto — Sala de Estudos Virtual

Objetivo: criar uma plataforma onde pessoas possam entrar em salas virtuais para estudar juntas, escolher um personagem, conversar em tempo real, ouvir música e acompanhar uma sessão de estudo.

🛠️ Stack principal
🐍 Python
🌐 Flask
🗄️ PostgreSQL
⚡ Flask-SocketIO / WebSockets
🎨 HTML5 + CSS3
🟨 JavaScript apenas onde for necessário para as interações em tempo real
🔐 Flask-Login / autenticação
🧪 Pytest para testes
🚀 Git + GitHub
☁️ Deploy no final
🗺️ Roteiro completo — do zero ao Deploy
🟢 FASE 1 — Planejamento
Aula 1 — Planejamento do projeto

Vamos definir:

Nome do projeto
Objetivo
Funcionalidades
Tecnologias
Arquitetura
Estrutura de pastas
Fluxo do usuário
MVP

Resultado: teremos o mapa completo antes de programar.

🟢 FASE 2 — Preparação do ambiente
Aula 2 — Criando o projeto Python

Vamos configurar:

Pasta do projeto
Ambiente virtual .venv
Flask
Dependências
.gitignore
requirements.txt
Git
Repositório GitHub

Estrutura inicial:

sala-estudos/
│
├── app/
├── static/
├── templates/
├── tests/
├── .env
├── .gitignore
├── requirements.txt
└── run.py
🟢 FASE 3 — Banco de dados
Aula 3 — PostgreSQL

Vamos instalar/configurar:

PostgreSQL
Banco do projeto
Usuário
Senha
Variáveis de ambiente
Conexão Python → PostgreSQL
Aula 4 — Modelagem do banco

Vamos criar as tabelas:

users
avatars
rooms
room_users
messages
study_sessions

E entender os relacionamentos.

Exemplo:

USUÁRIO
   │
   ├── possui AVATAR
   │
   ├── entra em SALAS
   │
   └── envia MENSAGENS
🟢 FASE 4 — Sistema de usuários
Aula 5 — Cadastro

Criar:

Nome de usuário
E-mail
Senha
Validação
Hash da senha

Nada de guardar senha em texto puro.

Aula 6 — Login

Criar:

Tela de login
Autenticação
Sessão
Logout
Proteção das páginas
🟢 FASE 5 — Personagens
Aula 7 — Sistema de personagens

O usuário poderá escolher seu personagem.

Exemplo:

🧑‍💻 Dev
👩‍🎓 Estudante
🧑‍🔬 Pesquisador
🎨 Criativo
📚 Leitor

Vamos salvar a escolha no banco.

🟢 FASE 6 — Salas
Aula 8 — Criando as salas

Criar salas como:

📚 Sala Python
💻 Sala Programação
📊 Sala Dados
🎓 Sala Faculdade
🌙 Sala Noturna

Cada sala terá:

Nome
Descrição
Usuários
Status
Data de criação
Aula 9 — Entrar e sair da sala

O usuário poderá:

Entrar
   ↓
Sala
   ↓
Estudar
   ↓
Sair

Também vamos mostrar:

👥 5 pessoas estudando agora

🔥 FASE 7 — TEMPO REAL

Essa será uma das partes mais importantes do projeto.

Aula 10 — Flask-SocketIO

Vamos aprender:

WebSockets
Eventos
Conexões
Comunicação cliente/servidor
Aula 11 — Chat em tempo real

Dentro da sala:

┌──────────────────────────┐
│ 📚 Sala Python            │
├──────────────────────────┤
│ Maria: Bom estudo!       │
│ João: Valeu!             │
│ Wander: Vamos estudar 😎 │
├──────────────────────────┤
│ Digite uma mensagem...   │
│                    ENVIAR│
└──────────────────────────┘

A mensagem aparecerá para todos sem atualizar a página.

🔥 Aqui teremos um grande diferencial técnico.

Aula 12 — Usuários online

Vamos mostrar:

🟢 Wander
🟢 Maria
🟢 João
⚫ Carlos

E quando alguém entrar:

🟢 Maria entrou na sala.

Quando sair:

🔴 Maria saiu da sala.

🟢 FASE 8 — INTERFACE DA SALA
Aula 13 — Criando a sala virtual

Aqui o projeto começa a ficar bonito. 😎

Teremos algo parecido com:

┌──────────────────────────────────────────────┐
│ 📚 SALA PYTHON                         ⚙️    │
├──────────────────────────────────────────────┤
│                                              │
│        🧑‍💻       👩‍🎓       🧑‍🔬            │
│                                              │
│              📚 ESTUDANDO                    │
│                                              │
│                         ┌──────────────┐     │
│                         │    CHAT      │     │
│                         │              │     │
│                         │ João: Oi!    │     │
│                         │ Maria: Oi!   │     │
│                         └──────────────┘     │
│                                              │
├──────────────────────────────────────────────┤
│ 🎵 Música                  ⏱️ 25:00          │
└──────────────────────────────────────────────┘
🎵 FASE 9 — MÚSICA
Aula 14 — Player de música

Vamos criar:

Play
Pause
Volume
Próxima música
Música ambiente

Inicialmente podemos trabalhar com áudios licenciados/permitidos para uso.

⏱️ FASE 10 — POMODORO
Aula 15 — Cronômetro de estudos

Teremos:

       25:00

       ▶️

FOCO

Depois:

       05:00

     ☕ PAUSA

Podemos permitir que a sala tenha uma sessão coletiva.

🟢 FASE 11 — MELHORIAS
Aula 16 — Perfil do usuário

Criar:

Avatar
Nome
Status
Tempo estudado
Salas frequentadas
Aula 17 — Melhorias na experiência

Vamos trabalhar:

Responsividade
Animações
Feedback visual
Loading
Mensagens
Estados vazios
Mobile

Aqui vamos deixar com aparência de produto real, não de projeto de curso.

🔐 FASE 12 — SEGURANÇA
Aula 18 — Segurança

Vamos revisar:

Senhas
.env
SQL Injection
XSS
Validação
Sessões
Autorização
Dados enviados pelo usuário
🧪 FASE 13 — TESTES
Aula 19 — Testes automatizados

Vamos testar:

Cadastro
Login
Logout
Salas
Mensagens
APIs
Regras do sistema

Usaremos Pytest.

🟢 FASE 14 — API
Aula 20 — API do projeto

Vamos criar endpoints para coisas como:

GET    /api/rooms
GET    /api/rooms/<id>
POST   /api/rooms
GET    /api/users

Isso também reforça sua experiência com APIs em Python.

📦 FASE 15 — ORGANIZAÇÃO FINAL
Aula 21 — Refatoração

Vamos revisar o projeto inteiro:

Código
Pastas
Banco
Segurança
Performance
Organização
Remover código desnecessário
Aula 22 — README profissional

O GitHub terá:

Descrição
Objetivo
Tecnologias
Funcionalidades
Screenshots
Arquitetura
Banco de dados
Como instalar
Como executar
Variáveis de ambiente
API
Autor
🚀 FASE 16 — DEPLOY
Aula 23 — Preparando produção

Vamos configurar:

Variáveis de ambiente
PostgreSQL de produção
requirements.txt
Servidor
Configurações de produção
Aula 24 — Deploy

Colocar o projeto online.

Depois vamos testar:

Computador 1
      ↓
     Sala
      ↑
Computador 2

E verificar se o chat realmente funciona em tempo real.

🔥 Esse teste vai ser muito legal.

💼 FASE 17 — PORTFÓLIO
Aula 25 — GitHub profissional

Vamos organizar:

Repositório
README
Commits
Imagens
Descrição
Topics
Projeto publicado
Aula 26 — LinkedIn

Vamos preparar a apresentação do projeto:

Projeto: Sala de Estudos Virtual

E destacar:

Python + Flask + PostgreSQL + WebSockets + autenticação + comunicação em tempo real.

🏆 RESULTADO FINAL

No final, teremos algo assim:

                    SALA DE ESTUDOS
                           │
          ┌────────────────┼────────────────┐
          │                │                │
       Usuário           Salas          Personagem
          │                │                │
          └────────────────┼────────────────┘
                           │
                     Sala Virtual
                           │
          ┌────────────────┼────────────────┐
          │                │                │
         Chat            Música          Pomodoro
          │                │                │
          └────────────────┼────────────────┘
                           │
                      PostgreSQL
                           │
                        Flask
                           │
                     WebSockets
                           │
                         Deploy