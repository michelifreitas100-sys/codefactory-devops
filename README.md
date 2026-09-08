# CodeFactory Solutions — Task Manager API

## 📋 Descrição do projeto
Este repositório contém a prova de conceito desenvolvida pela consultoria de
DevOps contratada pela **CodeFactory Solutions** para demonstrar a adoção da
**Cultura DevOps** no fluxo de desenvolvimento da empresa.

O projeto é uma pequena **API de gerenciamento de tarefas** (Task Manager),
usada como aplicação de exemplo para demonstrar, na prática, versionamento
colaborativo, containerização e integração contínua.

## 🎯 Objetivo
Mostrar como práticas e ferramentas DevOps (Git/GitHub, Docker e pipelines de
CI) resolvem os problemas relatados pela CodeFactory Solutions:
- ausência de padronização entre desenvolvedores;
- dificuldade de integrar o trabalho da equipe;
- ambientes de desenvolvimento demorados para configurar;
- falta de documentação e automação de testes/entregas.

## 🛠️ Tecnologias utilizadas
- **Python 3.12 / Flask** — API da aplicação;
- **PostgreSQL** — banco de dados;
- **Docker e Docker Compose** — containerização;
- **GitHub Actions** — pipeline de Integração Contínua;
- **Git/GitHub** — versionamento e colaboração (branches, PRs, Issues, Wiki,
  Projects).

## 📁 Estrutura de pastas
```
codefactory-devops/
├── app/
│   ├── main.py              # API Flask (rotas /, /health, /tasks)
│   ├── init_db.py           # script que cria as tabelas no banco
│   ├── requirements.txt     # dependências da aplicação
│   └── requirements-db.txt  # dependências do container de inicialização do banco
├── tests/
│   └── test_app.py          # testes automatizados (usados pela pipeline de CI)
├── .github/
│   └── workflows/
│       └── ci.yml           # pipeline de Integração Contínua (GitHub Actions)
├── Dockerfile                # imagem da aplicação
├── Dockerfile.db-init        # imagem do container que inicializa o banco
├── docker-compose.yml        # orquestra app + banco + inicializador
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Instruções de instalação

### Pré-requisitos
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) e Docker Compose
- (Opcional, para rodar localmente sem Docker) Python 3.12+

### Clonando o repositório
```bash
git clone https://github.com/SEU-USUARIO/codefactory-devops.git
cd codefactory-devops
```

## ▶️ Instruções de execução

### Opção 1 — Rodando com Docker Compose (recomendado)
```bash
docker compose up --build
```
Isso irá subir três containers:
- `codefactory_app` — a API, disponível em `http://localhost:5000`;
- `codefactory_db` — o banco PostgreSQL;
- `codefactory_db_init` — cria as tabelas no banco e encerra.

### Opção 2 — Rodando localmente (sem Docker)
```bash
cd app
pip install -r requirements.txt
python main.py
```

### Testando a API
```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Minha primeira tarefa"}'
curl http://localhost:5000/tasks
```

### Rodando os testes automatizados
```bash
pip install -r app/requirements.txt pytest
pytest tests/ -v
```

## 🔄 Integração Contínua
A cada `push` ou `pull request` para as branches `main` e `desenvolvimento`,
a pipeline definida em `.github/workflows/ci.yml` executa automaticamente:
1. checkout do código;
2. instalação das dependências;
3. lint do código (flake8);
4. execução dos testes automatizados (pytest);
5. build da imagem Docker, validando o `Dockerfile`.

## 🌱 Estratégia de branches
- `main` — versão estável, protegida por Pull Request;
- `desenvolvimento` — branch de integração das novas funcionalidades;
- `features/*` — uma branch por funcionalidade (ex.: `features/criar-tarefa`).

## 📄 Licença
Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para
mais detalhes.

Nome: Micheli de Freitas RU:5298211
fghf
