# 🏥 Assistente de Medicamentos CLI (A.M.C.)

[![Build Status](https://github.com/th-mFerreira/assistente-medicamentos-cli/actions/workflows/ci.yml/badge.svg)](#)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](#)
[![Python](https://img.shields.io/badge/python-3.12+-yellow.svg)](#)
[![Database](https://img.shields.io/badge/database-supabase--postgres-00C58E.svg)](#)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](#)

> *Precisão, segurança e confiabilidade na gestão de prontuários médicos através de persistência relacional em nuvem.*

---

**🟢 Status do Deploy:** Online | **🚀 Acesso Rápido:** [Rodar Aplicação no Navegador via Replit](https://replit.com/@miguelfloliveir/assistente-medicamentos-cli)

> **💡 Instrução de Uso na Nuvem (Replit):** Como esta é uma aplicação CLI, ao abrir o link acima, clique na opção **"+ Tools & files"** (no centro da tela), selecione **"Shell"** no menu e digite o comando `python -m src.app` para iniciar o sistema no terminal virtualizado.

---

## 📖 Visão Executiva (Contexto Clínico)

Em ambientes hospitalares, clínicas de repouso ou no cuidado domiciliar de alta complexidade, a administração de medicamentos exige rigor absoluto. Erros de dosagem, confusão de horários ou a fragmentação do histórico medicamentoso representam riscos severos à integridade do paciente.

O **Assistente de Medicamentos CLI** foi arquitetado como uma solução tecnológica para mitigar a falha humana. Operando através de uma interface de linha de comando (CLI) de alta responsividade e baixo consumo de recursos, o sistema garante a centralização de prontuários, validação estrita de dosagens via regras de negócio e a persistência segura dos dados.

Na sua versão atual, o ecossistema evoluiu de um modelo local estático para uma arquitetura distribuída resiliente, conectando a aplicação diretamente a um **Banco de Dados Relacional em Nuvem**, simulando com fidelidade os níveis de segurança e concorrência exigidos em softwares de missão crítica.

---

## ✨ Principais Funcionalidades

- **🛡️ Validação Restrita de Entradas:** Bloqueia proativamente o cadastro de dosagens nulas/negativas e turnos inválidos, evitando falhas humanas de prescrição.
- **☁️ Persistência Relacional (DBaaS):** Integração nativa com o **Supabase (PostgreSQL)**, garantindo que os dados de pacientes e medicamentos sejam persistidos de forma relacional, segura e acessível de qualquer nó de execução.
- **🖥️ Interface Rica e Ergonométrica:** Desenvolvida sobre a biblioteca `Rich`, oferecendo painéis dinâmicos, tabelas coloridas e formatação visual avançada para reduzir a fadiga ocular do operador clínico.
- **🔄 Governança e Integração Contínua (CI):** Pipeline automatizada via GitHub Actions que executa testes de regressão com isolamento de ambiente (Mocks) e análise estática rigorosa de código a cada Pull Request.

---

## 🏗️ Arquitetura e Stack Tecnológico

O projeto adota o princípio de Separação de Conceitos (Separation of Concerns - SoC), assegurando alta coesão e baixo acoplamento entre as camadas de domínio, infraestrutura e apresentação.

| Tecnologia | Função no Ecossistema |
| :--- | :--- |
| **Python 3.12+** | Linguagem base, escolhida por sua robustez, legibilidade e tipagem. |
| **Supabase** | Provedor de Banco de Dados na nuvem (PostgreSQL) para persistência estável. |
| **Rich** | Motor de renderização e estilização da Interface de Linha de Comando (CLI). |
| **Pytest** | Framework de automação de testes com abordagem focada em regressão. |
| **Ruff** | Linter e analisador estático ultra-rápido desenvolvido em Rust para garantia de estilo. |
| **Python-Dotenv** | Gerenciador de segurança para isolamento de credenciais e variáveis de ambiente. |

---

## 🚀 Guia de Implantação Local (Getting Started)

Para provisionar e rodar este software em uma máquina local, siga criteriosamente o protocolo de inicialização abaixo:

> ⚠️ **Pré-requisitos:** Certifique-se de ter o **[Git](https://git-scm.com/)** e o **[Python 3.12+](https://www.python.org/downloads/)** instalados e configurados globalmente no `PATH` do seu sistema operacional.

### 1. Clonagem do Repositório
```bash
git clone [https://github.com/th-mFerreira/assistente-medicamentos-cli.git](https://github.com/th-mFerreira/assistente-medicamentos-cli.git)
cd assistente-medicamentos-cli
