from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(file("EXO-16-023_temp.pdf", "rb"))

# print the title of document1.pdf
print "title = %s" % (input1.getDocumentInfo().title)

# add page 1 from input1 to output document, unchanged
output.addPage(input1.getPage(0))


# print how many pages input1 has:
print "document1.pdf has %s pages." % input1.getNumPages()

# finally, write "output" to document-output.pdf
outputStream = file("document-PAS.pdf", "wb")
output.write(outputStream)
outputStream.close()

