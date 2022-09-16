from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
import re
import os

path = r'C:\xxx'

page_lst =[]
checkImg = r"/Subtype(?= */Image)"
pdf = fitz.open(path + r'\公司年报.PDF')
lenXREF = pdf._getXrefLength()
for  i  in  range(lenXREF):
        text = pdf._getXrefString(i)
    isImage = re.search(checkImg, text)
    if  isImage:
            page_lst.append(i)

print(page_lst)

pdf_reader = PdfFileReader(path + r'\公司年报.PDF')
for  page  in  page_lst:
        pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(page))
    with open(path + r'\公司年报_{}.pdf'.format(page + 1),  'wb') as out:
            pdf_writer.write(out)
