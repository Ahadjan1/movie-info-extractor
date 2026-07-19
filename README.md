# 🎬 Movie Info Extractor

An AI-powered tool that extracts structured movie information (name, year, director, genre, cast, plot) from either a movie name or a descriptive paragraph — using LangChain Prompt Templates and Structured Output Parsing.

🔗 **Live Demo:** [movie-info-extractor-x.streamlit.app](https://movie-info-extractor-x.streamlit.app/)

## 📊 Overview

This project demonstrates two different approaches to getting information out of an LLM:

1. **Plain Text Output** — using `ChatPromptTemplate` with System + Human roles, returning a formatted text response
2. **Structured Output** — using Pydantic schemas (`with_structured_output`) to get clean, typed, machine-readable JSON

A toggle lets the user switch between the two output modes in real time.

## 🧠 Features

- Accepts either a **movie name** or a **paragraph** describing a movie
- **Plain Text mode:** Human-readable formatted response
- **Structured mode:** Typed Pydantic schema output + Raw JSON view
- Handles missing information gracefully (marks fields as "Not mentioned" instead of guessing)

## 🏗️ Tech Stack

- LangChain + `langchain-mistralai`
- Mistral AI (`mistral-small-latest`)
- Pydantic (schema validation for structured output)
- Streamlit (Frontend)

## 🚀 Running Locally

```bash
git clone https://github.com/Ahadjan1/movie-info-extractor.git
cd movie-info-extractor
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
streamlit run movie_extractor_combined.py

## 👤 Author

**Ahad Jan**
- GitHub: [@Ahadjan1](https://github.com/Ahadjan1)
- LinkedIn: [Ahad Jan](https://www.linkedin.com/in/ahad-jan-b8ba872b4/)
```

You'll need a free Mistral API key — add it to a `.env` file:
