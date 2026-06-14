# 🏥 Assistente de Medicamentos CLI (A.M.C.)

[![Build Status](https://github.com/th-mFerreira/assistente-medicamentos-cli/actions/workflows/ci.yml/badge.svg)](#)
[![Python](https://img.shields.io/badge/python-3.12+-yellow.svg)](#)
[![Database](https://img.shields.io/badge/database-supabase--postgres-00C58E.svg)](#)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](#)

> *Precisão, segurança e confiabilidade na gestão de medicamentos através de persistência relacional em nuvem.*

---

## 📖 Visão Geral

O **Assistente de Medicamentos CLI (A.M.C.)** é uma aplicação desenvolvida em Python para auxiliar no gerenciamento de pacientes e medicamentos por meio de uma interface de linha de comando moderna, segura e intuitiva.

O sistema foi projetado para reduzir erros operacionais relacionados ao controle de medicações, centralizando informações essenciais em uma única plataforma e aplicando validações de negócio para garantir a integridade dos dados cadastrados.

Sua arquitetura evoluiu de um modelo baseado em armazenamento local para uma solução conectada a um **Banco de Dados Relacional PostgreSQL hospedado no Supabase**, proporcionando persistência segura, escalabilidade e aderência às práticas utilizadas em aplicações corporativas modernas.

---

## ✨ Principais Funcionalidades

- **🛡️ Validação de Regras de Negócio:** Impede o cadastro de dosagens inválidas e informações inconsistentes.
- **☁️ Persistência em Nuvem:** Integração com Supabase (PostgreSQL) para armazenamento confiável dos dados.
- **👤 Gerenciamento de Pacientes:** Cadastro e consulta de pacientes.
- **💊 Controle de Medicamentos:** Registro e acompanhamento de medicamentos prescritos.
- **🖥️ Interface Aprimorada:** Utilização da biblioteca `Rich` para exibição de tabelas, painéis e mensagens formatadas.
- **🧪 Testes Automatizados:** Cobertura das principais regras de negócio e camada de persistência.
- **🔄 Integração Contínua:** Execução automática de testes e verificações de qualidade através do GitHub Actions.

---

## 🏗️ Arquitetura e Stack Tecnológica

O projeto foi estruturado seguindo o princípio de **Separation of Concerns (SoC)**, promovendo alta coesão e baixo acoplamento entre os componentes da aplicação.

| Tecnologia | Função |
| :--- | :--- |
| **Python 3.12+** | Linguagem principal da aplicação |
| **Supabase** | Banco de dados PostgreSQL em nuvem |
| **Rich** | Interface visual para terminal |
| **Pytest** | Framework de testes automatizados |
| **Ruff** | Linter e análise estática de código |
| **Python-Dotenv** | Gerenciamento de variáveis de ambiente |

---

## 🚀 Guia de Implantação Local (Getting Started)

Para executar o projeto localmente, siga as etapas abaixo.

> ⚠️ **Pré-requisitos:** Possuir o Git e o Python 3.12+ instalados e configurados no sistema.

## 1️. Clonagem do Repositório
```bash
git clone https://github.com/th-mFerreira/assistente-medicamentos-cli.git
cd assistente-medicamentos-cli
```

## 2️. Criação do Ambiente Virtual
### Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate
### Linux/macOS
python -m venv venv
source venv/bin/activate

## 3. Instalação das Dependências
python -m pip install --upgrade pip
pip install -r requirements.txt

## 4. Inicialização da Aplicação
python -m src.app

## 🧪 Garantia de Qualidade (QA & Testing)

A confiabilidade do sistema é assegurada por uma suíte de testes automatizados responsável por validar:

### Regras de negócio
Tratamento de exceções
Persistência de dados
Integração entre componentes
#### Executar os testes
python -m pytest -v
#### Executar análise estática
ruff check .

## 📂 Estrutura do Projeto
```bash
assistente-medicamentos-cli/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   └── persistence.py
├── tests/
│   ├── test_models.py
│   └── test_persistence.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔄 Integração Contínua

O projeto utiliza GitHub Actions para automatizar:

Execução de testes
Verificação de qualidade do código
Validação de Pull Requests
Garantia de estabilidade da branch principal

## 👨‍💻 Autor

Miguel Ferreira

Estudante de Engenharia de Software e desenvolvedor focado em desenvolvimento web, automação de processos e soluções baseadas em Inteligência Artificial.

GitHub: https://github.com/th-mFerreira

"Tecnologia aplicada para tornar o gerenciamento de medicamentos mais seguro, organizado e confiável."
