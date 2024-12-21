from PyPDF2 import PdfWriter, PdfReader
pdfwriter=PdfWriter()
pdf=PdfReader("SamplePDF.pdf")
for page_num in range(len(pdf.pages)):
  pdfwriter.add_page(pdf.pages[page_num])
passw=input('Enter password to protect pdf : ')
pdfwriter.encrypt(passw)
with open('High.pdf','wb') as f:
  pdfwriter.write(f)