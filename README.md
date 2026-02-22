# Customer Support Triage System

An LLM-powered backend service that automatically **classifies incoming customer support messages** by category and priority, and generates a concise summary. The system is built with **FastAPI**, **LangChain (modern core)**, and a **vLLM-hosted open-source model**, designed to be modular, extensible, and production-ready.

---

## ✨ Features (Currently Implemented)

* 🔍 **Automated Triage**

  * Categorizes customer messages into:

    * `Billing`
    * `Technical`
    * `Account`
    * `Other`
  * Assigns a priority level:

    * `High`, `Medium`, `Low`

* 🧠 **LLM-Powered Reasoning**

  * Uses an instruction-tuned open-source model
  * Deterministic inference (`temperature=0`) for stability

* ⚡ **FastAPI Backend**

  * Simple REST API interface
  * Ready to be extended with async, middleware, and auth

* 🔌 **vLLM + OpenAI-Compatible API**

  * Works with self-hosted models via OpenAI-style endpoints

---

## Flow:

1. API receives a customer message
2. Message is passed to the LangChain triage chain
3. LLM classifies and summarizes the message
4. Structured JSON response is returned

---

## 📦 Tech Stack

* **Python** 3.10+
* **FastAPI** – API framework
* **LangChain** – Prompting & chaining
* **vLLM** – High-performance model serving
* **Streamlit** – Simple UI

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd Customer-Support-Triage-System
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the API server

```bash
uvicorn api.app:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

---

## 🧪 Example Request

```json
POST /triage
{
  "message": "I was charged twice for my subscription this month"
}
```

### Example Response

```json
{
  "category": "Billing",
  "priority": "High",
  "summary": "Customer reports being charged twice for a subscription",
  "confidence": 0.85
}
```

> ⚠️ Note: `confidence` is currently a placeholder value.

---

## 📄 Current Limitations

* Confidence score is static (not model-derived yet)
* No persistence (results are not stored)
* No authentication
* Synchronous processing only

---

## 🔮 Future Improvements (Planned)

### 1. Overcoming all current limitations.
### 2. Adding a RAG agent on top of current system to solve frequently asked queries and for new queries and queries at which RAG agent fails, triage system will work.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements, bug fixes, or documentation improvements.

---

## 📜 License

MIT License (or your preferred license)

---

## 🙌 Acknowledgements

* LangChain
* FastAPI
* vLLM
* Open-source LLM community
