import pdfplumber

def load_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # avoid None pages
                text += page_text + "\n"

    return text

if __name__ == "__main__":
    pdf_path = "data/sample.pdf"
    content = load_pdf(pdf_path)
    print(content[:1000]) 

