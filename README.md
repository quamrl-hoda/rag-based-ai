## RAG-Based AI Tutor for Sigma Web Development Course

This project is a **Retrieval-Augmented Generation (RAG)–based AI teaching assistant** built for the **Sigma Web Development Course**.

It allows users to ask **course-specific questions**, and the system:

* Finds the **most relevant video chunks** (using embeddings)
* Identifies **video number + timestamps**
* Generates **grounded answers** using an LLM
* Rejects **out-of-course questions**

---

## Features

* Video → Audio → Text pipeline (Whisper)
* Chunked transcripts with timestamps
* Semantic search using embeddings (Ollama `bge-m3`)
* Cosine similarity for relevance ranking
* LLM-generated answers (Gemini / Ollama)

---

## Project Structure

```text
rag-based-ai/
│
├── audios/                 # Extracted audio files (.mp3)
├── videos/                 # Original course videos
├── whisper/                # Whisper model / configs
│
├── jsons/                  # Chunked transcript JSON files
│
├── embeddings.joblib       # Stored embeddings for all chunks
│
├── video_to_mp3.py         # Convert video → audio (FFmpeg)
├── mp3_to_json.py          # Transcribe audio → timestamped text
├── preprocess_json.py      # Clean & chunk transcript JSON
├── stt.py                  # Speech-to-text logic
│
├── process_incoming.py     # Handles user query → retrieval → LLM
│
├── prompt.txt              # System / RAG prompt template
├── response.txt            # Latest generated response
├── output.json             # Example processed output
│
├── sample.py               # Experiments / testing
│
├── .env                    # API keys (NOT committed)
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── LICENSE                 # License
└── README.md               # Project documentation
```

---

## 🔁 System Workflow

```text
User Question
   ↓
Text Embedding (Ollama: bge-m3)
   ↓
Cosine Similarity Search
   ↓
Top Relevant Video Chunks
   ↓
Prompt Construction (with timestamps)
   ↓
LLM Response (Gemini / Ollama)
   ↓
Final Answer + Video Guidance
```

---

## Technologies Used

* **Python**
* **Whisper** – speech-to-text
* **FFmpeg** – audio extraction
* **Ollama** – local embeddings (`bge-m3`)
* **Gemini LLM** – response generation
* **scikit-learn** – cosine similarity
* **NumPy / Pandas**
* **Joblib** – embedding storage

---

## Setup Instructions

###  Clone the repository

```bash
git clone <repo-url>
cd rag-based-ai
```

###  Create & activate environment

```bash
conda create -n ragai_env python=3.10
conda activate ragai_env
```

###  Install dependencies

```bash
pip install -r requirements.txt
```

### Set environment variables

Create `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

---

##  Ollama Setup (Required)

### Start Ollama

```bash
ollama serve
```

### Pull embedding model

```bash
ollama pull bge-m3
```

Verify:

```bash
ollama list
```

---

## How to Run the Project

### Step 1: Convert videos to audio

```bash
python video_to_mp3.py
```

### Step 2: Generate transcripts

```bash
python mp3_to_json.py
```

### Step 3: Preprocess & chunk transcripts

```bash
python preprocess_json.py
```

### Step 4: Generate embeddings

(inside preprocessing / separate script)

### Step 5: Ask questions

```bash
python process_incoming.py
```

---

##  Example Question

```text
Where is semantic HTML taught in this course?
```

### Example Answer

```text
Semantic HTML is not taught in Video 6 (SEO and Core Web Vitals).
This video focuses on meta tags and SEO concepts.
```


##Scope Control

❗ The assistant **only answers questions related to the Sigma Web Development Course**.
Unrelated questions are rejected politely.

---

## 📌 Future Improvements

* FAISS / Chroma vector DB
* Confidence scoring
* Clickable timestamps
* UI (Streamlit / Web app)
* Chat memory
* Multi-course support


## License

This project is licensed under the **Apache License**.

