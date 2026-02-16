# ⚡ ARQuizMaster - AI Discord Quiz Solver

O **ARQuizMaster** é uma automação inteligente para Discord desenvolvida em Python. Ele utiliza a tecnologia do **Google Gemini 1.5 Flash** via API REST para identificar perguntas de quizzes (especialmente do LordBot) em tempo real e enviar a resposta correta de forma automatizada.



## 🚀 Funcionalidades

* **Extração de Embeds**: Capaz de ler títulos, descrições e campos (fields) de mensagens de bots.
* **Integração com Gemini 1.5 Flash**: Utiliza a IA mais rápida da Google para respostas em milissegundos.
* **Conexão via API REST**: Evita erros comuns de bibliotecas instáveis (como erro 404) através de requisições diretas via `aiohttp`.
* **Delay Humano**: Configuração de tempo de espera (sleep) para evitar detecções de anti-cheat.
* **Filtros Inteligentes**: Ignora mensagens de placar, avisos de tempo e foca apenas em rodadas ativas.

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: [Python](https://www.python.org/)
* **Biblioteca Discord**: `discord.py-self`
* **Comunicação API**: `aiohttp` (Asynchronous HTTP Client)
* **IA Generativa**: [Google Gemini API](https://ai.google.dev/)

## 📋 Pré-requisitos

Antes de começar, você precisará:
1. Uma **API Key** do Google Gemini (Obtenha no [Google AI Studio](https://aistudio.google.com/)).
2. Seu **Token** de conta do Discord.
3. Python 3.10 ou superior instalado.

## 🔧 Instalação e Configuração

1. **Clone o repositório**:
   ```bash
   git clone [https://github.com/zLestDev/QuizSniper.git](https://github.com/zLestDev/QuizSniper.git)
   cd ARQuizMaster
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install discord.py-self aiohttp
   ```

4. **Configure o 'bot.py'**
Insira seu TOKEN, GEMINI_KEY e o CANAL_ID nas variáveis de configuração no topo do arquivo.

## 🏃 Execução
Para iniciar o bot, você pode usar o terminal:
   ```bash
   python bot.py
   ```

Ou utilizar o arquivo **LigarBot.bat** (incluso na raiz) para um início rápido com dois cliques.

---

## 🛡️ Aviso Legal (Disclaimer)
Este projeto foi desenvolvido para fins de estudo e automação pessoal. O uso de "self-bots" pode violar os Termos de Serviço do Discord. Use com responsabilidade.

---
