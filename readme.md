# 🦙 Local Chat — Ollama + LangChain + Streamlit

A fully local AI chat app with conversation memory, model switching,
and streaming output. No API keys. No cloud. Runs on your machine.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red)
![LangChain](https://img.shields.io/badge/LangChain-Ollama-green)

![Demo](/demo.png)

## Features

- Streaming responses — words appear as they generate
- Conversation memory — model remembers full chat context
- Model switcher — swap between any Ollama model from sidebar
- Temperature control — tune creativity vs precision
- Custom system prompt — change the AI's personality
- Clear chat — wipe history and start fresh

## How it work




## Setup

### 1. Install Ollama and pull a model
Download from https://ollama.com and run:
```bash
ollama pull llama3.2
```

### 2. Clone and set up Python environment
```bash
git clone https://github.com/YOUR_USERNAME/ollama-chat
cd ollama-chat
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run
```bash
streamlit run app.py
```

Open http://localhost:8501

## Tech stack

| Tool | Role |
|------|------|
| Ollama | Local LLM runtime |
| LangChain | LLM abstraction + message history |
| Streamlit | Chat UI + session state |
| Llama 3.2 | Default model (swappable) |

## What I learned building this

- How LLM memory works — it's not magic, it's sending the full
  conversation history on every request
- How token streaming works with generators
- How Streamlit session_state persists data across reruns
- The difference between system prompts, human messages, and AI messagess
