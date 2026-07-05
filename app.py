from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_pdf_text
from utils.docx_reader import extract_docx_text
from utils.txt_reader import extract_txt_text
from utils.text_preprocessing import preprocess_text
from utils.database import create_database, insert_document
from utils.search import search_keyword

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create database and table
create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("document")

    if file is None or file.filename == "":
        return "<h2>No file selected!</h2>"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    filename = file.filename.lower()

    # Extract text
    if filename.endswith(".pdf"):
        text = extract_pdf_text(filepath)

    elif filename.endswith(".docx"):
        text = extract_docx_text(filepath)

    elif filename.endswith(".txt"):
        text = extract_txt_text(filepath)

    else:
        return "<h2>Unsupported file type!</h2>"

    # Preprocess text
    cleaned_text = preprocess_text(text)

    # Chunk text
    chunk_size = 500
    chunks = []

    for i in range(0, len(cleaned_text), chunk_size):
        chunks.append(cleaned_text[i:i + chunk_size])

    # Store chunks in database
    for chunk in chunks:
        insert_document(file.filename, chunk)

    return f"""
    <h2>File Uploaded Successfully!</h2>

    <p><b>Filename:</b> {file.filename}</p>

    <p><b>Total Chunks:</b> {len(chunks)}</p>

    <h3>First Chunk:</h3>

    <pre>{chunks[0] if chunks else 'No text found in the document.'}</pre>
    """
@app.route("/search")
def search_page():
    return render_template("search.html")


@app.route("/search", methods=["POST"])
def search():

    keyword = request.form["keyword"]

    results = search_keyword(keyword.lower())

    return render_template(
        "search.html",
        results=results,
        searched=True
    )

if __name__ == "__main__":
    app.run(debug=True)