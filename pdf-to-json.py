import fitz
import json


def extract_text_from_pdf(pdf_path):
    text_data = []
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        page_text = page.get_text()
        text_data.append(page_text)

    pdf_document.close()
    return text_data


def save_text_to_json(text_data, json_path):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(text_data, json_file, ensure_ascii=False, indent=4)


pdf_path = 'example.pdf'
json_path = 'output.json'

extracted_text = extract_text_from_pdf(pdf_path)
save_text_to_json(extracted_text, json_path)
