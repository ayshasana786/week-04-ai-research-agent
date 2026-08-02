# 🤖 AI Research Agent using LangGraph

An AI-powered Research Agent built using **LangGraph**, **LangChain**, **Groq Llama 3.3**, **Wikipedia**, and **DuckDuckGo**. The agent researches a user’s query, collects information from multiple sources, and generates a clear summarized response.

---

## 🚀 Features

- AI-powered research assistant
- Multi-source information retrieval
- Wikipedia search
- DuckDuckGo search
- Summarization using Groq Llama 3.3
- LangGraph workflow
- Conditional routing
- Agent memory
- Command Line Interface (CLI)

---

## 🛠️ Technologies Used

- Python
- LangGraph
- LangChain
- Groq API
- Wikipedia API Wrapper
- DDGS (DuckDuckGo Search)
- python-dotenv

---

## 📂 Project Structure

```
Week-04-AI-Research-Agent/
│
├── app.py
├── graph.py
├── nodes.py
├── state.py
├── tools.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## 🔄 Workflow

```
User Question
      │
      ▼
Planner Node
      │
      ▼
Research Node
      │
      ├── Wikipedia
      └── DuckDuckGo
      │
      ▼
Summary Node
      │
      ▼
Final Response
```

---

## 🧠 LangGraph Nodes

### Planner Node
- Receives the user's question.
- Plans the research process.
- Initializes the agent state.

### Research Node
- Searches Wikipedia.
- Searches DuckDuckGo.
- Collects information from multiple sources.
- Stores research results.

### Summary Node
- Uses Groq Llama 3.3.
- Summarizes the collected research.
- Generates the final response.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/week-04-ai-research-agent.git
```

Go to the project folder:

```bash
cd week-04-ai-research-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
python app.py
```

---

## 💻 Example

**Input**

```
What is Machine Learning?
```

**Output**

- Researches using Wikipedia
- Searches DuckDuckGo
- Collects relevant information
- Generates a summarized response

---

## 📌 Future Improvements

- Add Google Search integration
- Support research paper search
- Export summaries as PDF
- Build a Streamlit web interface
- Add conversation memory

---

## 👩‍💻 Author

**Aysha Sana**

M.Sc. Computer Science (Data Analytics)

Generative AI | AI/ML | Python | LangGraph | LangChain