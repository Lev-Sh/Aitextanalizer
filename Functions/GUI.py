import tkinter as tk
from tkinter import filedialog
from pypdf import PdfReader
root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF Files", "*.pdf")])
if path:
  print("File path : ", path)
else : print("No file selected")
reader = PdfReader(path)
print(f"There is {len(reader.pages)}Pages")
page = reader.pages[0]
print(page.extract_text())
for i in range(len(reader.pages)):
    page = reader.pages[i]
    print(page.extract_text())
