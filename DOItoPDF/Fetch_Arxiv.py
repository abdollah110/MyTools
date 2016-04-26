import urllib2
from urllib2 import urlopen, HTTPError
from urllib2 import Request
import http.cookiejar
import datetime
import re
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import io


JHEP="http://link.springer.com/content/pdf/"
PRL="http://journals.aps.org/prl/pdf/"
PRD="http://journals.aps.org/prd/pdf/"
PRC="http://journals.aps.org/prc/pdf/"
EPJC="http://link.springer.com/content/pdf/"
JINST="http://iopscience.iop.org/article/"
arXive="http://arxiv.org/pdf/"



def getPLBURL(journal,doi,count):
    
    cj = http.cookiejar.CookieJar() # initialize the cookie jar
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    url = 'http://dx.doi.org/'+doi
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = [('User-Agent', user_agent)]
    opener.addheaders = headers
    #with opener.open(url) as response:
    response= opener.open(url)
    output = response.read()
    import re
    p = re.compile('pdfurl="(.*?)"')
    m = p.search(output.strip().decode('utf-8')) # need to convert from bytes to string
    m.group(1)
    response=opener.open(m.group(1))
    out = response.read()

    type(out)

    f = io.BytesIO(out)

    if f:
        o = PdfFileReader(f)
        merged = PdfFileWriter()
        outName= "Single_"+str(count)+".pdf"
        merged.addPage(o.getPage(0))
        with open(outName,'wb') as pdf:
            merged.write(pdf)




def getOtherURL(journal,doi,count):


    strTT = journal+doi
    out = urllib2.urlopen(strTT)
    fileM = open('FullPaper.pdf', 'w')
    fileM.write(out.read())
    fileM.close()
    
    
    output = PdfFileWriter()
    input1 = PdfFileReader(file("FullPaper.pdf", "rb"))
    
    # add page 1 from input1 to output document, unchanged
    if input1:
        outName= "ARXIV_Single_"+str(count)+".pdf"
        output.addPage(input1.getPage(0))
        outputStream = file(outName, "w")
        output.write(outputStream)
        outputStream.close()


def getSimpleJINST(journal,doi,count):
    
    strTT = journal+doi+"/pdf"
    out = urllib2.urlopen(strTT)
    fileM = open('FullPaper.pdf', 'w')
    fileM.write(out.read())
    fileM.close()
    
    
    output = PdfFileWriter()
    input1 = PdfFileReader(file("FullPaper.pdf", "rb"))
    
    # add page 1 from input1 to output document, unchanged
    if input1:
        outName= "Single_"+str(count)+".pdf"
        output.addPage(input1.getPage(1))
        outputStream = file(outName, "w")
        output.write(outputStream)
        outputStream.close()



NonFoundJournal = open("NonFoundJournal.txt", "w")
AllDOIList = open("AllDOIList.txt", "r")

count=0
for line in AllDOIList:
    if line[0]=="a" and line[1]=="r" and line[2]=="X":
        count += 1
        doi=line
        print "here is doi= " , doi
        newdoi=doi.replace("\n","")
        
        if "arXiv" in newdoi:
            url = 'abcdc.com'
            url = newdoi.replace('[hep-ex].', '')
            url2 = url.replace('arXiv:', '')
            
            getOtherURL(arXive,url,count)


        else:
            RemainingDOI.write(newdoi)
            print "######################### >>>>>>    not exist at all"

NonFoundJournal.close()






