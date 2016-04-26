
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

output = PdfFileWriter()


#Here is the name of all pdf that one needs to merge
TextSamples = open("pdfLists.txt", "r")
for line in TextSamples:

    print line.replace("\n","")
    append_pdf(PdfFileReader(file(line.replace("\n",""),"rb")),output)

output.write(file("combinedPDFs.pdf","wb"))

