# 🏥 Assistente de Medicamentos CLI (A.M.C.)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![Python](https://img.shields.io/badge/python-3.12+-yellow.svg)](#)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](#)

> *Precisão, segurança e confiabilidade na gestão de prontuários medicamentosos.*

---

# 🏥 Assistente de Medicamentos CLI (A.M.C.)
**🟢 Status:** Online | **🚀 Acesso Rápido:** [Rodar Aplicação no Navegador via Replit](https://replit.com/@miguelfloliveir/assistente-medicamentos-cli)

## 📖 Visão Executiva (Contexto Clínico)

Em ambientes hospitalares, clínicas de repouso ou no cuidado domiciliar de alta complexidade, a administração de medicamentos exige rigor absoluto. Erros de dosagem, confusão de horários ou a fragmentação do histórico medicamentoso representam riscos severos à segurança e integridade do paciente.

O **Assistente de Medicamentos CLI** foi arquitetado como uma solução tecnológica para mitigar a falha humana. Operando através de uma interface de linha de comando (CLI) de alta responsividade e baixo consumo de recursos, o sistema garante a centralização do prontuário, a validação estrita de dosagens via regras de negócio e a persistência segura dos dados.

## ✨ Principais Funcionalidades

- **🛡️ Validação Restrita de Entradas:** Bloqueia proativamente o cadastro de dosagens nulas/negativas e turnos inválidos, evitando falhas de prescrição.
- **💾 Persistência de Dados (Stateful):** Utilização de serialização em `.json` para garantir que os prontuários não sejam perdidos entre sessões.
- **🖥️ Interface Rica e Ergonométrica:** Desenvolvida com a biblioteca `Rich`, oferecendo painéis dinâmicos, tabelas coloridas e formatação visual que reduz a fadiga ocular do operador.
- **🔄 Integração Contínua (CI):** Pipeline configurada via GitHub Actions para garantia de qualidade estática e execução de testes de regressão a cada novo ciclo de desenvolvimento.

## 🏗️ Arquitetura e Stack Tecnológico

O projeto segue os princípios de separação de responsabilidades (SoC), garantindo alta coesão e baixo acoplamento:

| Tecnologia | Função no Ecossistema |
| :--- | :--- |
| **Python 3.12+** | Linguagem base, escolhida por sua robustez e legibilidade. |
| **Rich** | Motor de renderização da Interface de Linha de Comando (CLI). |
| **Pytest** | Framework de testes automatizados (Test-Driven approach). |
| **Ruff** | Linter e analisador estático ultra-rápido desenvolvido em Rust. |
| **JSON** | Banco de dados local/Armazenamento de estado. |

---

## 🚀 Guia de Implantação (Getting Started)

Para provisionar este software em uma máquina local ou terminal de operação clínico, siga o protocolo abaixo:

### 1. Clonagem do Repositório
```bash
git clone https://github.com/th-mFerreira/assistente-medicamentos-cli.git
cd assistente-medicamentos-cli

2. Isolamento de Ambiente (Virtual Environment)
É estritamente recomendado rodar a aplicação em um ambiente isolado para evitar conflitos de dependências em nível de sistema operacional.

Bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate

3. Instalação de Dependências
Bash
pip install --upgrade pip
pip install -r requirements.txt

4. Inicialização do Sistema
Bash
python -m src.app
🧪 Garantia de Qualidade (QA & Testing)
A integridade deste software é vitalícia e validada de forma contínua. Nossa suíte de testes cobre os Caminhos Felizes (Happy Paths), Casos de Erro (Error Handling) e Limites de Sistema (Edge Cases).

Para executar a bateria de testes unitários:

Bash
pytest -v
Para inspecionar a qualidade e padronização do código-fonte:

Bash
ruff check .
📂 Topologia do Projeto
Abaixo apresentamos a árvore de diretórios do repositório, refletindo um padrão profissional de engenharia de software:

Plaintext
assistente-medicamentos-cli/
├── .github/
│   └── workflows/
│       └── ci.yml             # Robô de Integração Contínua (GitHub Actions)
├── src/
│   ├── __init__.py
│   ├── app.py                 # Ponto de entrada (Entrypoint) e UI
│   ├── models.py              # Regras de Negócio e Entidades
│   └── persistence.py         # Camada de Dados (I/O)
├── tests/
│   ├── __init__.py
│   ├── test_models.py         # Testes de unidade das regras
│   └── test_persistence.py    # Testes de integração de dados
├── requirements.txt           # Manifesto de dependências
├── banco_medicamentos.json    # Banco de dados gerado automaticamente (ignorado no git)
└── README.md                  # Documentação oficial
👨‍💻 Autoria e Manutenção
Desenvolvido e mantido por [Miguel Ferreira].
Projeto arquitetado como requisito de excelência para a disciplina de Bootcamp II - Engenharia de Software.

Código aberto, focado em salvar o recurso mais valioso: o tempo.
=======
Para provisionar este software em uma máquina local ou terminal de operação clínico, siga o protocolo de inicialização abaixo.

> ⚠️ **Pré-requisitos de Sistema:** Certifique-se de ter o **[Git](https://git-scm.com/)** e o **[Python 3.12+](https://www.python.org/downloads/)** instalados e configurados no `PATH` da sua máquina antes de prosseguir.

## 1. Clonagem do Repositório
Faça o download do código-fonte para a sua máquina local acessando o repositório oficial:

git clone https://github.com/th-mFerreira/assistente-medicamentos-cli.git

cd assistente-medicamentos-cli

## 2. Isolamento de Ambiente (Virtual Environment)
É estritamente recomendado provisionar a aplicação dentro de um ambiente virtual isolado. Isso previne conflitos de dependências com outras aplicações no nível do sistema operacional (SO).
Selecione a aba correspondente ao seu SO:

🔹 Para ambientes Windows:
PowerShell

python -m venv venv

.\venv\Scripts\activate

🔹 Para ambientes Linux / macOS (POSIX):
Bash

python -m venv venv

source venv/bin/activate

O ambiente estará isolado com sucesso quando o prefixo (venv) aparecer no início da linha do seu terminal.

## 3. Resolução de Dependências
Com o ambiente ativado, atualize o gerenciador de pacotes e instale as dependências rigorosamente fixadas no manifesto corporativo:


python -m pip install --upgrade pip

pip install -r requirements.txt

## 4. Inicialização do Sistema
Execute o ponto de entrada principal para iniciar o motor da Interface de Linha de Comando (CLI):


python -m src.app

## 🧪 Garantia de Qualidade (QA & Testing)
A integridade deste software é considerada crítica e validada de forma contínua. Nossa suíte de testes automatizados cobre sistematicamente os Caminhos Felizes (Happy Paths), Tratamento de Exceções (Error Handling) e Casos Limite (Edge Cases).

Para executar a bateria de testes unitários e de integração de dados:


pytest -v

Para inspecionar a padronização, complexidade ciclomática e acurácia do código-fonte (Análise Estática):


ruff check .

## 📂 Topologia da Arquitetura
A estrutura de diretórios foi desenhada sob o padrão arquitetural de Separação de Conceitos (Separation of Concerns - SoC), garantindo alta coesão e baixo acoplamento entre as camadas de dados, domínio e apresentação:

```text
assistente-medicamentos-cli/
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de Integração Contínua (GitHub Actions)
├── src/
│   ├── __init__.py
│   ├── app.py                 # Camada de Apresentação (CLI Engine & UI)
│   ├── models.py              # Camada de Domínio (Entidades e Regras de Negócio)
│   └── persistence.py         # Camada de Infraestrutura (I/O de Dados em JSON)
├── tests/
│   ├── __init__.py
│   ├── test_models.py         # Asserções rigorosas de regras de negócios
│   └── test_persistence.py    # Asserções de integridade do Banco de Dados
├── requirements.txt           # Manifesto oficial de dependências do ecossistema
├── banco_medicamentos.json    # Banco de Dados de estado dinâmico (Ignorado no Git)
└── README.md                  # Documentação Técnica e Executiva
```

## 👨‍💻 Autoria e Manutenção
Desenvolvido, mantido e arquitetado por [Miguel Ferreira].

Projeto submetido como requisito de excelência técnica estrutural para a disciplina de Bootcamp II - Engenharia de Software.

"Código aberto, estruturado para salvar o recurso mais crítico da saúde: o tempo."