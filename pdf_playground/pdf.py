import PyPDF2 #Install PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdfList):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfList:
        merger.append(pdf)
    
    merger.write('super.pdf')
    
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)



pdf_combiner(inputs)


