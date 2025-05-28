# 🤖 Multi-LLM AI Chatbot Platform

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com/)

**Created by [Bhupesh Danewa](https://linkedin.com/in/bhupesh-danewa)**  
*MTech AI, MANIT*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/bhupesh-danewa)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/bhupesh-danewa)

---

## 📋 Project Overview

An intelligent conversational AI platform that integrates multiple Large Language Model (LLM) providers with web search capabilities. Built with a scalable full-stack architecture featuring a RESTful API backend and responsive frontend interface.

### ✨ Key Features

- 🧠 **Multi-LLM Support**: Seamlessly switch between OpenAI and Groq models
- 🔍 **Web Search Integration**: Enhanced responses with real-time web data
- 🎯 **Customizable System Prompts**: Define AI agent behavior and role
- 💬 **Real-time Chat Interface**: Smooth conversational experience
- ⚡ **High-Performance Backend**: FastAPI-based RESTful architecture
- 🎨 **Modern UI/UX**: Clean, intuitive Streamlit interface
- ☁️ **Cloud-Ready**: Easy deployment on Streamlit Cloud

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Frontend** | Streamlit |
| **Backend** | Python, FastAPI |
| **AI/ML** | LangGraph, OpenAI API, Groq API |
| **Web Search** | Custom search integration |
| **Environment** | Python 3.11, Conda |

## 🏗️ Architecture

```
┌─────────────────┐    HTTP/REST    ┌─────────────────┐    API Calls    ┌─────────────────┐
│   Streamlit     │ ──────────────► │   FastAPI       │ ──────────────► │   LLM Providers │
│   Frontend      │                 │   Backend       │                 │   (OpenAI/Groq) │
│   (UI/UX)       │ ◄────────────── │   (Business     │ ◄────────────── │                 │
└─────────────────┘    JSON         │    Logic)       └─────────────────┘                 │
                                     │                 │                                     │
                                     │                 │    API Calls    ┌─────────────────┐
                                     │                 │ ──────────────► │   Web Search    │
                                     │                 │ ◄────────────── │   Services      │
                                     └─────────────────┘                 └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Conda (recommended)
- OpenAI API Key
- Groq API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/bhupeshdanewa07/ai-chatbot-platform.git
   cd ai-chatbot-platform
   ```

2. **Create conda environment**
   ```bash
   conda create -n chatbot-env python=3.11
   conda activate chatbot-env
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Add your API keys to .env
   OPENAI_API_KEY=your_openai_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   # Terminal 1: Start backend
   python backend.py
   
   # Terminal 2: Start frontend
   streamlit run frontend.py
   ```


## 📁 Project Structure

```
ai-chatbot-platform/
├── 📄 frontend.py          # Streamlit UI application
├── 📄 backend.py           # FastAPI backend server
├── 📄 agentic_ai.py        # AI agent logic and LLM integration
├── 📄 requirements.txt     # Python dependencies
├── 📄 .env.example         # Environment variables template
├── 📄 README.md           # Project documentation
└── 📁 __pycache__/        # Python cache (auto-generated)
```

## 🎯 Usage

### 1. Configure Your AI Agent
- Enter a system prompt to define your AI agent's behavior
- Example: *"You are a helpful coding assistant specializing in Python development"*

### 2. Select LLM Provider & Model
- **Groq**: Ultra-fast inference
  - `llama-3.3-70b-versatile`
  - `mixtral-8x7b-32768`
- **OpenAI**: Advanced reasoning
  - `gpt-4o`

### 3. Enable Web Search (Optional)
- Toggle web search for real-time information retrieval
- Enhances responses with current data

### 4. Start Chatting
- Enter your query and click "Ask Agent!"
- Receive intelligent, contextual responses

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API authentication key | Yes |
| `GROQ_API_KEY` | Groq API authentication key | Yes |
| `API_URL` | Backend API endpoint | No (default: localhost) |

### Model Configuration

The application supports multiple models with different capabilities:

- **Groq Models**: Optimized for speed and efficiency
- **OpenAI Models**: Advanced reasoning and complex tasks


## 📊 Features Showcase

### Multi-Provider Support
Switch seamlessly between different AI providers and models based on your needs.

### Intelligent Web Search
Enhance AI responses with real-time web data for up-to-date information.

### Customizable Behavior
Define your AI agent's personality and expertise through system prompts.

### Professional Interface
Clean, modern UI built with Streamlit for optimal user experience.


## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [LangChain](https://langchain.com/) for LLM integration tools
- [OpenAI](https://openai.com/) for powerful language models
- [Groq](https://groq.com/) for ultra-fast inference

## 📈 Future Enhancements

- [ ] Add more LLM providers (Anthropic Claude, Google PaLM)
- [ ] Implement conversation history
- [ ] Add file upload capabilities
- [ ] Multi-language support
- [ ] Advanced prompt templates library
- [ ] User authentication system
- [ ] Analytics dashboard

---

<div align="center">

**Built with ❤️ by [Bhupesh Danewa](https://linkedin.com/in/bhupesh-danewa)**

*If you found this project helpful, please consider giving it a ⭐!*

</div>
