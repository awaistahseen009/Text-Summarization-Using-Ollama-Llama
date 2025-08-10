# LLaMA Text Summarizer

This is a simple AI project that uses the LLaMA model (via Ollama) to summarize text.
It has:

- A **FastAPI backend**
- A **Streamlit frontend**
- Local **LLaMA model via Ollama**

---

## 🚀 Quick Start

1. **Install Ollama**
   - Download and install Ollama from [https://ollama.com](https://ollama.com) and make sure it is running on your device.
2. **Clone the repo**
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app**
   ```bash
   ./start.sh
   ```
   This script will:
   - Ensure the LLaMA model is downloaded
   - Start the backend and frontend in parallel

---

## 🐳 Docker

You can also run everything in Docker:

```bash
# Build the Docker image
sudo docker build -t llama-text-summarizer .

# Run the container (make sure Ollama is running on your host!)
sudo docker run --network=host llama-text-summarizer
```

> **Note:** Ollama must be installed and running on your host machine. The Docker container expects to connect to Ollama at `localhost:11434`.

---

## 🧪 Running Tests

To run all backend and frontend tests:

```bash
pytest tests/
```

---

## 🛠️ Backend (FastAPI)

![Backend](images/backend.png)

- Handles summarization requests by talking to the LLaMA model via LangChain and Ollama.
- Runs on [http://localhost:8000](http://localhost:8000)
- Endpoint: `/summarize/`

---

## 🎨 Frontend (Streamlit)

![Frontend](images/frontend.png)

- User-friendly interface for entering text and viewing summaries.
- Runs on [http://localhost:8501](http://localhost:8501)

---

## 📦 Project Structure

```
text-summarizer-llama/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── images/
│   ├── backend.png
│   └── frontend.png
│
├── tests/
│   ├── test_backend.py
│   └── test_frontend.py
│
├── venv/
│
├── requirements.txt
├── Dockerfile
├── start.sh
└── README.md
```

---

## 💡 Tips

- Always start Ollama before running the app or Docker container.
- The backend and frontend will both be available as long as the model is downloaded and Ollama is running.
- For best results, keep your Ollama and model versions up to date!
