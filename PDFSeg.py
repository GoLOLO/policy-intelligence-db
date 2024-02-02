import requests
from PyPDF2 import PdfReader, PdfWriter
import pdfplumber
import os

def download_pdf(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded '{local_filename}'")

def split_pdf(local_filename):
    reader = PdfReader(local_filename)
    num_pages = len(reader.pages)
    split_dir = f"{local_filename}_split"
    os.makedirs(split_dir, exist_ok=True)

    for page_number in range(num_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_number])

        output_filename = os.path.join(split_dir, f"page_{page_number + 1}.pdf")
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)

    print(f"Split '{local_filename}' into {num_pages} separate page files")
    return num_pages, split_dir

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text

def save_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

# Use the functions
pdf_url = 'https://drive.google.com/uc?export=download&id=125JJ3pP9o3lrM4NF4PkoUSF53ZTdwmG2'
pdf_filename = 'document.pdf'
download_pdf(pdf_url, pdf_filename)
_, split_dir = split_pdf(pdf_filename)

# Extract text from split PDFs
text_dir = f"{split_dir}_text"
os.makedirs(text_dir, exist_ok=True)

for pdf_file in sorted(os.listdir(split_dir)):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(split_dir, pdf_file)
        text = extract_text_from_pdf(pdf_path)
        text_filename = pdf_file.replace(".pdf", ".txt")
        text_path = os.path.join(text_dir, text_filename)
        save_text_to_file(text, text_path)

        print(f"Extracted text from {pdf_path} and saved to {text_path}")

