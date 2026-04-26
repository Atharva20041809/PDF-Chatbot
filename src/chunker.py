
import pdfplumber

def load_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


if __name__ == "__main__":
    pdf_path = "data/sample.pdf"

    content = load_pdf(pdf_path)
    chunks = chunk_text(content)

    print("Total chunks:", len(chunks))
    print("\nFirst chunk:\n", chunks[0])