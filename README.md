# 📚 StudyRoom — Sala de Estudos Virtual

> **Estude junto. Não estude sozinho.**

O **StudyRoom** é uma plataforma de estudos colaborativos criada para proporcionar uma experiência mais interativa para pessoas que estudam sozinhas.

A proposta é permitir que usuários entrem em salas virtuais de estudo, escolham um personagem, encontrem outras pessoas estudando no mesmo ambiente, conversem através de um chat em tempo real, escutem música e utilizem ferramentas para melhorar a concentração.

Além disso, o StudyRoom está evoluindo para se tornar também uma **plataforma de aprendizagem para quem está começando em tecnologia**, com trilhas de estudo organizadas (cursos, módulos e aulas), permitindo que o usuário siga um caminho estruturado de aprendizado, além de estudar em comunidade.

---

## 🌐 Projeto no ar

Acesse a versão em produção: **https://studyroom-uhio.onrender.com**

> ⚠️ Hospedado no plano gratuito do Render — o servidor "dorme" após um período de inatividade, então o primeiro acesso pode demorar alguns segundos para carregar.

🚧 **Projeto em desenvolvimento contínuo** — novas trilhas e funcionalidades sendo adicionadas aos poucos.

---

## 🎯 Objetivo

Criar uma experiência de estudo compartilhado, proporcionando a sensação de estar estudando junto com outras pessoas, mesmo que cada usuário esteja em seu próprio ambiente — combinando isso com trilhas de aprendizagem estruturadas para iniciantes em tecnologia.

---

## 🚀 Funcionalidades

### Já implementadas
* 👤 Cadastro e login de usuários, com senha protegida por hash
* 🔐 Sessão de usuário e proteção de rotas
* 🎓 Trilhas de aprendizagem com módulos e aulas em PDF (conteúdo autoral)
* 🧭 Navegação entre páginas com menu dinâmico
* ☁️ Deploy em produção (Render)

### Planejadas
* 🧑‍💻 Escolha de personagem/avatar
* 🏠 Salas virtuais de estudo
* 👥 Usuários online
* 💬 Chat em tempo real (Flask-SocketIO)
* 🎵 Música ambiente
* ⏱️ Cronômetro Pomodoro
* 📊 Registro de sessões de estudo
* 📈 Registro de progresso do usuário nas trilhas
* 🌐 API REST
* 🧪 Testes automatizados

---

## 🛠️ Tecnologias

### Backend
* 🐍 Python
* 🌐 Flask
* ⚡ Flask-SocketIO *(planejado)*
* 🐘 PostgreSQL
* 🔌 Psycopg
* 🔐 Python-dotenv
* 🔒 Werkzeug Security (hash de senha)
* 🦄 Gunicorn (servidor de produção)

### Frontend
* HTML5 (com herança de templates via Jinja)
* CSS3
* JavaScript

### Ferramentas
* Git
* GitHub
* VS Code
* pgAdmin 4
* Render (deploy e hospedagem)

---

## 🗄️ Banco de Dados

O projeto utiliza **PostgreSQL** como banco de dados principal — um banco local para desenvolvimento, e um banco na nuvem (Render) para produção.

### Tabelas atuais

```text
usuarios
│
├── id
├── nome
├── email
├── senha (hash)
└── data_criacao


trilhas
│
├── id
├── titulo
├── descricao
├── nivel
└── criado_em


modulos
│
├── id
├── trilha_id      → referencia trilhas(id)
├── titulo
└── ordem


aulas
│
├── id
├── modulo_id      → referencia modulos(id)
├── titulo
├── arquivo_pdf
└── ordem
```

As tabelas `trilhas`, `modulos` e `aulas` são conectadas por **chaves estrangeiras** (`REFERENCES`), garantindo que um módulo não possa existir sem uma trilha válida, e uma aula não possa existir sem um módulo válido.

As aulas usam conteúdo em **PDF autoral** (coluna `arquivo_pdf`, armazenado em `static/pdfs/`), no lugar de vídeos incorporados — evitando problemas de incorporação bloqueada e direitos autorais.

> 🔐 As credenciais do banco são armazenadas através de variáveis de ambiente (`.env` localmente, Environment Variables no Render). O arquivo `.env` não é enviado para o GitHub.

---

## 🔌 Conexão Python → PostgreSQL

A comunicação entre o Python e o PostgreSQL é realizada utilizando **Psycopg**. O arquivo `database.py` centraliza a conexão, lendo host, porta, nome do banco, usuário e senha inteiramente de variáveis de ambiente — isso permite usar o banco local durante o desenvolvimento e o banco na nuvem em produção, sem alterar uma linha de código.

```text
Python → database.py → python-dotenv → Psycopg → PostgreSQL
```

A rota `/teste-banco` valida a comunicação entre Flask e o banco, com tratamento de erros via `try/except`.

---

## 🔐 Autenticação: Cadastro, Login e Sessão

**Cadastro (`/cadastro`)**
- Captura `nome`, `email`, `senha` e `confirmar_senha` via `request.form`
- Valida se a senha e a confirmação de senha são iguais
- Gera um hash seguro da senha com `generate_password_hash` (Werkzeug) — a senha original nunca é salva no banco
- Insere o novo usuário no PostgreSQL com uma query parametrizada (`%s`), evitando SQL Injection

**Login (`/login`)**
- Busca o usuário no banco pelo `email` e compara a senha com `check_password_hash`
- Usa **mensagens de erro genéricas** ("E-mail ou senha incorretos"), evitando enumeração de usuários
- Ao validar com sucesso, guarda o `id` do usuário em `session["usuario_id"]` e redireciona para `/trilhas`

**Sessão e Logout**
- A sessão utiliza a `SECRET_KEY` (protegida via variável de ambiente) para assinar os dados
- A rota `/logout` remove o `usuario_id` da sessão e redireciona para o login

**Proteção de rotas (`@login_obrigatorio`)**
- Decorator personalizado, criado com `functools.wraps`, que redireciona para `/login` qualquer acesso sem sessão ativa
- Aplicado em todas as rotas que exigem autenticação (trilhas, detalhes da trilha)

---

## 🎓 Trilhas de Aprendizagem

Estrutura: `trilhas (1) ──< modulos (N) ──< aulas (N)`

**`/trilhas`** — lista todas as trilhas disponíveis em cards, protegida por `@login_obrigatorio`.

**`/trilha/<int:trilha_id>`** — busca a trilha, seus módulos (em ordem) e as aulas de cada módulo, exibindo o conteúdo de cada aula como um PDF incorporado na página (`<embed type="application/pdf">`), com um botão para abrir em tela cheia numa nova aba.

Trilha atual: **"Guia do zero ao primeiro projeto"**, com conteúdo autoral em PDF cobrindo os fundamentos de programação.

---

## 🧭 Templates e Navegação

O projeto usa **herança de templates do Jinja** (`{% extends %}` / `{% block %}`) para evitar duplicação de código entre páginas:

```text
base.html  (head, menu de navegação, mensagens flash, footer)
   │
   ├── index.html
   ├── login.html
   ├── cadastro.html
   ├── trilhas_lista.html
   └── trilha_detalhes.html
```

O menu de navegação, definido uma única vez no `base.html`, se adapta automaticamente ao estado da sessão (`{% if session.usuario_id %}`): mostra "Entrar/Criar conta" para visitantes, e "Trilhas/Sair" para usuários autenticados.

---

## ☁️ Deploy (Render)

A aplicação está hospedada no **Render**, com dois serviços conectados ao mesmo repositório GitHub:

- **Web Service**: roda a aplicação Flask via `gunicorn run:app`, com build automático a cada push na branch `main`
- **PostgreSQL**: banco de dados na nuvem, separado do banco local usado em desenvolvimento

**Arquivos de suporte ao deploy:**
- `requirements.txt` — dependências mínimas do projeto (Flask, psycopg, python-dotenv, Werkzeug, gunicorn), geradas manualmente para evitar poluição de bibliotecas de outros projetos
- `Procfile` — define o comando de start (`web: gunicorn run:app`)

**Variáveis de ambiente configuradas no Render**: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `SECRET_KEY` — nenhuma credencial fica exposta no código.

> 💡 **Lição aprendida durante o deploy:** o Windows (ambiente de desenvolvimento local) não diferencia maiúsculas/minúsculas em nomes de arquivo, mas o Linux (ambiente do Render) diferencia. Um `render_template("Cadastro.html")` com "C" maiúsculo funcionava local, mas quebrava em produção porque o arquivo real era `cadastro.html`. Corrigido padronizando todos os nomes de template em minúsculas.

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
├── Procfile
│
├── static/
│   ├── css/
│   ├── images/
│   │   └── foto_perfil.jpg
│   ├── js/
│   ├── music/
│   └── pdfs/
│       └── aula1_introducao.pdf
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── cadastro.html
│   ├── trilhas_lista.html
│   └── trilha_detalhes.html
│
├── tests/
│
├── ARQUITETURA.MD
└── ARQUITETURA(projeto).MD
```

> 🔐 O arquivo `.env` contém informações sensíveis e está protegido pelo `.gitignore`.

---

## 📌 Status do projeto

### Fase atual — Deploy concluído, expandindo conteúdo e funcionalidades

* [x] Planejamento e arquitetura inicial
* [x] Configuração do Flask e estrutura do projeto
* [x] Identidade visual da Home
* [x] PostgreSQL local configurado e testado
* [x] `database.py` com conexão via variáveis de ambiente
* [x] Sistema de cadastro completo (validação, hash, persistência)
* [x] Sistema de login completo (busca, validação de senha, mensagens genéricas)
* [x] Sessão de usuário (Flask `session`) e logout
* [x] Decorator `@login_obrigatorio` para proteger rotas
* [x] Modelagem das tabelas `trilhas`, `modulos` e `aulas` com chaves estrangeiras
* [x] Rota `/trilha/<id>` buscando trilha, módulos e aulas relacionadas
* [x] Rota `/trilhas` listando todas as trilhas em cards
* [x] Estilização das páginas de trilhas (CSS com grid, cards, badges)
* [x] Herança de templates (`base.html`) com menu de navegação dinâmico
* [x] Substituição de vídeos do YouTube por PDFs autorais (evita bloqueio de embed e direitos autorais)
* [x] `requirements.txt` e `Procfile` preparados para deploy
* [x] Banco PostgreSQL criado na nuvem (Render)
* [x] Deploy do Web Service no Render, com variáveis de ambiente configuradas
* [x] Projeto acessível publicamente em produção
* [ ] Mais trilhas de conteúdo (Banco de Dados, HTML/CSS, etc.)
* [ ] Registro de progresso do usuário nas trilhas
* [ ] Sistema de salas virtuais
* [ ] Chat em tempo real
* [ ] Sistema de personagens
* [ ] Player de música
* [ ] Pomodoro
* [ ] Testes automatizados

---

## 🎯 Próximos passos

Com o MVP no ar (autenticação + trilhas com conteúdo real, publicamente acessível), o foco agora é:

1. 📚 **Expandir o conteúdo** — criar novas trilhas (Banco de Dados, HTML/CSS, Lógica de Programação, etc.), cada uma com módulos e aulas em PDF autoral
2. 🧑‍🎨 **Refinar a experiência** — registro de progresso do usuário, talvez uma página de perfil
3. 🏠 **Funcionalidades sociais** — salas virtuais e chat em tempo real (Flask-SocketIO), conforme a visão original do projeto

O próximo grande projeto de portfólio planejado é um **e-commerce**, aplicando os mesmos princípios de MVP enxuto e boas práticas aprendidos aqui.

---

## 👨‍💻 Desenvolvedor

**Wander Farias**

Projeto desenvolvido para estudos, evolução profissional e construção de portfólio.

---

⭐ **StudyRoom está no ar e em desenvolvimento contínuo.**