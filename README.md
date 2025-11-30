# EduGuide - Knowledge Base Agent (WIP)
## Overview
EduGuide is a Knowledge Agent that answers Python basics questions from a PDF. 
It uses Flask for the backend and a clean HTML/CSS frontend. 
Users can type a question, and the agent provides answers based on the PDF content.

## Features & Limitations
- Supports 11 Python questions (demo PDF)
- Currently uses **mock responses** to avoid OpenAI quota limitations
- Frontend is interactive and stylish, with smooth scrolling and responsive design
- Designed to scale for more questions or larger PDFs in the future

## Tech Stack & APIs
- Python (Flask)
- HTML, CSS, JavaScript (frontend)
- OpenAI API ( commented for free-tier testing has integrated but due free usage limit couldn't display if openai api key provided this ai boat can answer all python related question sam like your looking for company details answering boat)


## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/EduGuide.git
cd EduGuide

2.Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux/Mac

3.Install dependencies:
pip install -r requirements.txt

4.Run the app locally:
python app.py

5.Open your browser and go to:
http://127.0.0.1:5000/


Architecture Diagram:

PDF (notes.pdf)
│
▼
Text Extraction & Chunking
│
▼
Embeddings / Mock Answers
│
▼
Similarity Search & Response
│
▼
Frontend Display (HTML/CSS/JS)

  short explanation:  
Explanation of blocks:
- PDF → The source document with Python Q&A
- Text Extraction & Chunking → App reads PDF, splits content into smaller chunks
- Embeddings / Mock Answers → Converts text to embeddings 
- Similarity Search & Response → Finds the most relevant chunk and generates the answer
- Frontend Display → User types question → sees answer in the browser


## Potential Improvements
- Integrate full OpenAI embeddings and GPT-4 for dynamic answers from any PDF
- Support larger PDFs and multiple subjects
- Enhance frontend with more styling and animations
- Add user authentication to save previous queries
