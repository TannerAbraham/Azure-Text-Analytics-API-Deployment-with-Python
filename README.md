Azure Cognitive Services Text Analysis API project using FastAPI in Python

---

````markdown
# Azure Text Analysis API with FastAPI

This project provides a FastAPI-based interface to interact with **Azure Cognitive Services – Text Analytics API**. It enables sentiment analysis, language detection, key phrase extraction, and entity recognition through a lightweight, async-enabled Python backend.

## 🔍 Features

- ✅ Sentiment Analysis  
- 🌍 Language Detection  
- 🗝️ Key Phrase Extraction  
- 🧠 Named Entity Recognition  
- ⚡ High-performance async API using FastAPI + uvloop  
- ☁️ Integration with Azure Cognitive Services Text Analytics

---

## 🛠️ Tech Stack

- FastAPI – Web framework for building APIs
- Azure Cognitive Services – Cloud-based NLP
- uvicorn + gunicorn – ASGI servers for production
- aiohttp – Asynchronous HTTP client
- pydantic – Data validation and serialization

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Azure Cognitive Services account with endpoint and key

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/azure-text-analysis-api.git
   cd azure-text-analysis-api
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Azure credentials:

   ```env
   AZURE_API_KEY=your_azure_api_key
   AZURE_ENDPOINT=https://your-resource-name.cognitiveservices.azure.com/
   ```

---

## 🧪 Usage

Start the API locally with:

```bash
uvicorn main:app --reload
```

Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

### Example Request (via Swagger UI or `curl`)

```json
POST /analyze

{
  "documents": [
    {
      "id": "1",
      "language": "en",
      "text": "FastAPI is amazing for building modern APIs!"
    }
  ]
}
```

---

## 🧾 Endpoints

| Method | Endpoint   | Description                        |
| ------ | ---------- | ---------------------------------- |
| POST   | `/analyze` | Runs all supported Azure NLP tasks |
| GET    | `/health`  | Health check endpoint              |

---

## 📁 Project Structure

```
.
├── main.py              # FastAPI app and routing
├── utils.py             # Azure interaction logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧰 Development & Deployment

### Run with Gunicorn (for production):

```bash
 main:app -k uvicorn.workers.UvicornWorker
```

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for more information.

---

## ✨ Acknowledgments

* [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)
* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Pydantic](https://docs.pydantic.dev/)

```

---

Let me know if you want this README auto-populated with example responses or deployment via Docker.
```
