from pdf_processing import extract_text_from_file

pdf = "data/UNIT 4.pdf"

with open (pdf, "rb") as file:
    text = extract_text_from_file(file)
    print(text)


