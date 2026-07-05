# Construction Safety Document Intelligence
## Project Overview
Construction Safety Document Intelligence is a Flask-based web application that helps process construction safety documents. Users can upload PDF, DOCX, and TXT files. The application extracts text from these documents, preprocesses the text, stores it in an SQLite database, and prepares it for searching.

## Features
- Upload PDF, DOCX, and TXT documents
- Extract text from uploaded documents
- Preprocess extracted text
- Store processed text in an SQLite database
- Generate a searchable knowledge repository

## Technologies Used
- Python
- Flask
- HTML
- CSS
- SQLite
- PyMuPDF (for PDF text extraction)
- python-docx (for DOCX text extraction)

## Project Structure
project-construction-safety-document-intelligence/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── knowledge.db
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── search.html
│
└── utils/
    ├── database.py
    ├── pdf_reader.py
    ├── docx_reader.py
    ├── txt_reader.py
    ├── text_preprocessing.py
    └── search.py

## Installation
1. Clone the repository
git clone <repository-url>
2. Navigate to the project folder
cd project-construction-safety-document-intelligence
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
5. Open your browser and visit
http://127.0.0.1:5000

## Future Improvements
- Image upload with OCR
- AI-powered document summarization
- Keyword search interface
- User authentication
- Dashboard for uploaded documents

## Author
Developed by Indravathi Meesala
