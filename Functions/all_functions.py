import requests
from pypdf import PdfReader
def pdf_to_str(path: str = ""):
    reader = PdfReader(path)
    page = reader.pages[0]
    result = ''
    result += page.extract_text()
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        result += page.extract_text()
    return result
def url_to_str(url: str = ""):
    link = url
    f = requests.get(link)
    content = f.text
    return content

def doc_to_str():
    pass

