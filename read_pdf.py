#!/usr/bin/env python3
import sys
import os

# Try different PDF libraries
try:
    import PyPDF2
    def read_pdf_pypdf2(filepath):
        with open(filepath, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
            return text
    print(read_pdf_pypdf2(sys.argv[1]))
    sys.exit(0)
except ImportError:
    pass

try:
    import pdfplumber
    def read_pdf_plumber(filepath):
        text = ""
        with pdfplumber.open(filepath) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text() or ""
        return text
    print(read_pdf_plumber(sys.argv[1]))
    sys.exit(0)
except ImportError:
    pass

print("Error: No PDF library found. Please install PyPDF2 or pdfplumber:", file=sys.stderr)
print("  pip3 install PyPDF2", file=sys.stderr)
print("  or", file=sys.stderr)
print("  pip3 install pdfplumber", file=sys.stderr)
sys.exit(1)


