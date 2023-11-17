#Merge PDFs in folder the file is saved in

import PyPDF2
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write("merged.pdf") 
