from pypdf import PdfReader
reader = PdfReader("example.pdf")
print(f"There is {len(reader.pages)}Pages")
page = reader.pages[0]
print(page.extract_text())
for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.extract_text())
