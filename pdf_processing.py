import PyPDF2

def extract_text_from_file(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text+=page.extract_text()
        return text
    
    except Exception as e:
        return f"Error extracting text {e}"
    
    