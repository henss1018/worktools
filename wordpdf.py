#!python3
import os,PyPDF2

#加密后的pdf用minipdf打不开。。。
def encryppdf():
    os.chdir('D:\\python\\test')
    for foldername, subfolders, filenames in os.walk("D:\\python\\test"):
        for filename in filenames:
            if(os.path.splitext(filename)[1] == '.pdf'):
                pdffile = open(filename, 'rb')
                pdfreader = PyPDF2.PdfFileReader(pdffile)
                pdfwriter = PyPDF2.PdfFileWriter()
                for pagenum in range(4):
                    pdfwriter.addPage(pdfreader.getPage(pagenum))
                pdfwriter.encrypt('aaa')
               # resultpdf = open('encryped_'.join(filename), 'wb')
                resultpdf = open('encryped_docker.pdf', 'wb')
                pdfwriter.write(resultpdf)
                resultpdf.close()
                pdffile.close()


encryppdf()