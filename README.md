# Complete RAG Tutorial

A step-by-step Retrieval-Augmented Generation (RAG) project built from scratch — from document ingestion to retrieval. Each stage of the pipeline is implemented and explained in order.

**Stack:** LangChain · OpenAI embeddings · ChromaDB

## Pipeline stages

| # | Stage | Status | Where |
|---|-------|--------|-------|
| 1 | Load documents from `docs/` | ✅ done | `load_documents()` in `ingestion_pipeline.py` |
| 2 | Split into chunks | 🚧 in progress | `split_documents()` (drafted in `ingestion_pipeline.py`) |
| 3 | Embed chunks (OpenAI) | 🚧 in progress | `embed_chunks()` (drafted in `ingestion_pipeline.py`) |
| 4 | Store in vector DB (Chroma) | ⏳ next | — |
| 5 | Retrieval (semantic search) | ⏳ next | — |

## Project structure

```
RAG/
├── ingestion_pipeline.py      # Stages 1–4: load → chunk → embed → store
├── docs/                      # Sample documents to ingest
│   ├── Google.txt
│   ├── Microsoft.txt
│   ├── Nvidia.txt
│   ├── SpaceX.txt
│   ├── Tesla.txt
│   └── attention-is-all-you-need.pdf
├── requirements.txt           # Pinned Python dependencies
├── .env                       # API keys (gitignored)
└── .gitignore
```

## Setup

1. **Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure `.env`** (already gitignored, never commit it):

   ```
   OPENAI_API_KEY=sk-...
   ```

## Run

```bash
python ingestion_pipeline.py
```

Currently loads all `*.txt` files from `docs/` and prints a preview of each document.

## Notes

- `DirectoryLoader` currently globs `*.txt` only — the PDF in `docs/` will need a PDF loader (e.g. `PyPDFLoader`) once multi-format ingestion is in scope.
- Chunking defaults (drafted): `chunk_size=1000`, `chunk_overlap=200`.
