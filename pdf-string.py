import pathlib
from pypdf import PdfReader

pdf_path = input("Enter the path to the PDF file: ")
pdf_file = pathlib.Path(pdf_path)

#checking if file exists
if pdf_file.exists():
    print("File exists!")
else : print("File does not exist!")

reader = PdfReader(pdf_file)
print(f"There is {len(reader.pages)}Pages")
page = reader.pages[0]
print(page.extract_text())
for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.extract_text())