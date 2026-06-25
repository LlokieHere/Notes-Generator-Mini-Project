# 📝 Notezz - AI Notes Generator

A desktop application that transforms your raw notes into structured study materials using AI.

## ✨ Features
- Paste your notes and get an AI-powered summary
- Customize output with checkboxes:
  - 📌 Simple Concepts
  - 🔗 Analogy
  - 💡 Example
  - 📖 Definitions
  - ❓ Practice Questions

## 🛠️ Built With
- Python
- PySide6 (Qt for Python)
- Groq API (LLaMA 3.3 70B)

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/LlokieHere/Notes-Generator-Mini-Project.git
cd Notes-Generator-Mini-Project

### 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate

### 3. Install dependencies
pip install PySide6 groq python-dotenv

### 4. Set up your API key
Get your free API key at console.groq.com
Create a .env file based on .env.example

GROQ_API_KEY=your_api_key_here

### 5. Run the app
python main.py

## ⚠️ Notes
- Never commit your .env file
- Free tier allows generous requests per day
