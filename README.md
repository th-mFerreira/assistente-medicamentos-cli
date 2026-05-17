# 🏥 Assistente de Medicamentos CLI (A.M.C.)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![Python](https://img.shields.io/badge/python-3.12+-yellow.svg)](#)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](#)

> *Precisão, segurança e confiabilidade na gestão de prontuários medicamentosos.*

---

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