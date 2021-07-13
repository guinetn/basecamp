
# https://levelup.gitconnected.com/5-programs-for-processing-pdf-file-with-python-54ce9bb7ef67

# create
pip install reportlab

from reportlab.pdfgen import canvas
report = canvas.Canvas("file1.pdf")
report.drawString(50, 800, "This is an example for Medium")
report.save()   

# merge
pip install PyPDF2
from PyPDF2 import PdfFileReader, PdfFileMerger

first_file = PdfFileReader("file1.pdf")
second_file = PdfFileReader("file2.pdf")

output = PdfFileMerger()

output.append(first_file)
output.append(second_file)
output.write("new_merged.pdf")    