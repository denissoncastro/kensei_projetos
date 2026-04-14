﻿# ⛩️ Kensei Lab: Operações em Python ⛩️

Este repositório contém uma coleção de scripts desenvolvidos para o laboratório **Kensei**, focados em automação, lógica de programação e fundamentos de cybersecurity. Cada módulo foi construído seguindo princípios de **Clean Architecture** e interface via terminal com estética hacker.

---

## 📂 Estrutura de Módulos

### 1. 📂 Organizador de Arquivos (`file_organizer.py`)
Módulo de automação que realiza a triagem de diretórios bagunçados.
*   **Funcionalidade:** Varre uma pasta e move arquivos para subpastas específicas (Imagens, Docs, Vídeos, etc.) baseando-se na extensão.
*   **Destaque:** Gera um log final detalhando quantos arquivos foram movidos por categoria.
*   **Tecnologias:** `os`, `shutil`.

### 2. 🔐 Gerador de Senhas (`password_generator.py`)
Ferramenta para criação de chaves de acesso seguras.
*   **Funcionalidade:** Permite escolher o tamanho e a complexidade (Maiúsculas, Números, Símbolos).
*   **Destaque:** Gera um lote de 5 senhas de uma vez e as exporta para um arquivo `senhas.txt` com carimbo de data/hora (timestamp).
*   **Tecnologias:** `random`, `string`, `datetime`.

### 3. 🛡️ Cyber Quiz (`cyber_quiz.py`)
Simulador de avaliação de conhecimentos em segurança da informação.
*   **Funcionalidade:** 5 perguntas aleatórias sobre ataques e defesas com sistema de pontuação.
*   **Destaque:** Implementa um **Timer de 20 segundos** por pergunta usando Threads. Se o tempo esgotar, a questão é invalidada.
*   **Tecnologias:** `threading`, `random`, `sys`.

### 4. 📝 Lista de Compras (`shopping_list.py`)
Gerenciador simples de inventário ou tarefas.
*   **Funcionalidade:** Adicionar, visualizar e remover itens através de um menu interativo.
*   **Destaque:** Sincronização automática com arquivo `lista_compras.txt` ao encerrar o programa.
*   **Tecnologias:** Manipulação de Listas, I/O de arquivos.

### 5. 🌡️ Conversor Térmico (`celsius_to_fahrenheit.py`)
Calculadora de precisão para escalas de temperatura.
*   **Funcionalidade:** Conversão bidirecional entre Celsius e Fahrenheit.
*   **Destaque:** Validação rigorosa contra valores abaixo do **Zero Absoluto** e tratamento de erros para entradas não numéricas.
*   **Tecnologias:** Lógica matemática, `try-except`.

### 6. 👋 Hello User (`hello_user.py`)
Script de boas-vindas e validação inicial.
*   **Funcionalidade:** Solicita o nome do operador e retorna uma saudação formatada.
*   **Destaque:** Validação de comprimento mínimo de caracteres para garantir integridade dos dados.

---

## 🎨 Padrões Visuais
Todos os scripts utilizam códigos ANSI para estilização do terminal:
*   **Verde (`GREEN`):** Sucesso e Operações Concluídas.
*   **Ciano (`CYAN`):** Inputs e Prompts do Usuário.
*   **Vermelho (`RED`):** Alertas de Segurança e Erros.
*   **Negrito (`BOLD`):** Títulos e Destaques.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Navegue até a pasta do projeto.
3. Execute o script desejado:
   ```bash
   python nome_do_arquivo.py
   ```

---

## 🛡️ Missão do Lab
> "Transformar lógica pura em ferramentas de automação seguras e eficientes."

**Desenvolvido por:** Denisson Castro
**Projeto:** Kensei Lab

`Keep it stealthy. Keep it smart.`
