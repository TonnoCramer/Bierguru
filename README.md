# Vocatus AI — RAG-Enriched Django Chat App

Vocatus AI is a Django-based web application built to **understand how AI chatbots and agents work from the inside**, with a strong focus on **Retrieval-Augmented Generation (RAG)**, controlled context, and secure deployment.

This project is intentionally designed as a **learning and experimentation environment**, not as a black-box AI service.

---

## 1. Project Goals

This project explores:

- How a **Large Language Model (LLM)** functions as a reasoning and language-transformation engine
- How **RAG** can be used to inject explicit, auditable knowledge into an AI system
- How to separate **code, knowledge, and secrets** safely
- How to deploy an AI-enabled Django application securely on a VPS

The primary objective is understanding, not optimization or scale.

---

## 2. High-Level Architecture

The system is split into three clearly separated layers:

### Application Layer (Django)
- Django backend
- Chat interface (HTML / CSS / JavaScript)
- API endpoints connecting the frontend to AI logic

### Knowledge Layer (RAG)
- Private documents stored in `rag_source/`
- Embeddings and vector index stored in `rag_store/` (FAISS)

### LLM Layer
- External Large Language Model accessed via API
- Used only for interpretation, reasoning, and text generation

> RAG provides the knowledge.  
> The LLM processes and transforms that knowledge.

---

## 3. Chat Context & Memory Design

The chatbot operates as **one continuous conversation**, but with **explicitly limited memory**.

- The system keeps **only the last 6 messages** in context  
  (one system prompt plus the most recent user/assistant exchanges)
- Earlier conversation history is intentionally discarded

This design:

- Prevents uncontrolled context growth
- Keeps token usage and costs predictable
- Makes agent behavior transparent and debuggable

There is no hidden long-term memory.

---

## 4. Retrieval-Augmented Generation (RAG) Workflow

RAG is implemented as an explicit and reproducible pipeline:

1. Documents are placed in `rag_source/`  
   (private and not version-controlled)

2. The ingestion script is executed:
   ```bash
   python rag_ingest_all.py
   ```

3. Documents are chunked, embedded, and stored in a FAISS vector index (`rag_store/`)

4. At query time:
   - Relevant chunks are retrieved
   - Injected into the prompt
   - The LLM generates an answer **only** based on that context

This approach:

- Reduces hallucinations
- Improves explainability
- Keeps knowledge explicit and auditable

---

## 5. Version Control & Security Model

### Not included in GitHub

- `.env` (API keys and secrets)
- `rag_source/` (documents)
- `rag_store/` (embeddings and FAISS index)
- Local databases and virtual environments

### Included in GitHub

- Application code
- RAG ingestion logic (`rag_ingest_all.py`)
- Frontend assets
- Database migrations

> GitHub contains **how the system works**, not **what it knows**.

---

## 6. Deployment Philosophy

The application is designed to be deployed on a **private VPS**, with:

- Secrets managed via environment variables
- Restricted access where needed
- RAG stores generated per environment
- Clear separation between code, data, and configuration

Deployment is treated as a **learning process**, not just an end goal.

---

## Project Status

This is an **active learning project**.

Architectural changes, refactoring, and experiments are expected.  
Stability is secondary to **understanding and transparency**.

---

## Disclaimer

This project is intended for educational and experimental purposes only.  
It is not a production-ready AI service.
