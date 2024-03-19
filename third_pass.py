import pytesseract
from pdf2image import convert_from_path
import PyPDF2
import io

pdf_doc = r'files/Bradender_P1.pdf'
poppler_path=r"Release-24.02.0-0/poppler-24.02.0/Library/bin"
images = convert_from_path(pdf_doc, poppler_path=poppler_path)

pdf_writer = PyPDF2.PdfWriter()

for image in images:
    page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
    pdf = PyPDF2.PdfReader(io.BytesIO(page))
    pdf_writer.add_page(pdf.pages[0])

# export the searchable PDF to searchable.pdf
out_file = f'{pdf_doc[:-4]}_searchable.pdf'
with open(out_file, "wb") as f:
    pdf_writer.write(f)