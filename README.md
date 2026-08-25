# ⚡ AI-Powered Developer Portfolio & RAG Assistant

A modern, interactive developer portfolio featuring an embedded **Retrieval-Augmented Generation (RAG)** assistant. The AI answers visitor queries in real time using vector embeddings derived from my resume, technical skills, projects, and work experience.

🔗 **Live Demo:** https://portfolio-9ghg79bii-yash-250d.vercel.app

---

## 🚀 Features

- **Interactive AI Chat:** Real-time conversational agent grounded strictly in portfolio data.
- **RAG Pipeline Architecture:** Efficient document chunking, semantic vector search, and LLM-driven response generation.
- **Dynamic Source Attribution:** Displays source references (e.g., `resume.pdf`, `projects.txt`) alongside responses.
- **Serverless Backend:** FastAPI backend deployed alongside the React/Vite frontend on Vercel.
- **Responsive Dark UI:** Minimalist developer aesthetic with scannable project breakdowns and skill categories.

---

## 🛠️ Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React, Vite, Tailwind CSS, Lucide Icons |
| **Backend** | FastAPI, Python 3.12, Uvicorn |
| **AI / Embeddings** | Google Gemini API (`gemini-2.5-flash`, `gemini-embedding-001`) |
| **Vector Search** | FAISS (Facebook AI Similarity Search), NumPy |
| **Document Processing** | PyPDF |
| **Deployment** | Vercel (Frontend SPA + Python Serverless Functions) |

---

## 🧠 System Architecture

Knowledge Base (.txt / .pdf)
        │
        ▼
  Document Loader
        │
        ▼
     Chunker ────────► Gemini Embeddings ────────► FAISS Vector Store
                                                          │
Visitor Query ────────────────────────────────────────────┤
        │                                                 ▼
        ▼                                         Retrieved Chunks
Gemini Prompt Assembly ◄──────────────────────────────────┘
        │
        ▼
   LLM Response ──► Frontend UI with Citations

---

## 📁 Project Structure

.
├── api/                     # Vercel serverless entry point (index.py)
├── backend/
│   ├── api/                 # FastAPI routes (chat.py)
│   ├── llm/                 # Gemini API integration (model.py)
│   ├── rag/                 # RAG pipeline: chunker, embeddings, loader, retriever
│   ├── main.py              # FastAPI app definition & lifespan hooks
│   └── requirements.txt     # Backend Python dependencies
├── knowledge_base/          # Source documents (resume.pdf, projects.txt, etc.)
├── src/                     # React frontend source files
├── vercel.json              # Vercel routing and serverless rewrites
└── package.json             # Frontend dependencies and scripts

---

## ⚙️ Local Development Setup

### 1. Clone the Repository

git clone https://github.com/YASH-MV/PortFolio.git
cd PortFolio

### 2. Configure Environment Variables

Create a `.env` file inside the `backend/` directory:

GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
GEMINI_FALLBACK_MODEL=gemini-1.5-flash
GEMINI_EMBEDDING_MODEL=gemini-embedding-001
FRONTEND_ORIGIN=http://localhost:5173

### 3. Backend Setup

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

### 4. Frontend Setup

In a separate terminal window at the project root:

npm install
npm run dev

The application will run locally at http://localhost:5173.

---

## 🚢 Deployment (Vercel)

1. Push your repository to GitHub:
   git add .
   git commit -m "Add production README"
   git push origin main
2. In your Vercel Dashboard, navigate to **Settings → Environment Variables** and add `GEMINI_API_KEY`.
3. Vercel automatically deploys the static frontend build and provisions the Python serverless API.