from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader, PdfWriter


infile = PdfReader('no_sign.pdf', 'rb')
infile2 = PdfReader('signed.pdf', 'rb')
output = PdfWriter()

p2 = infile2.pages[0]

for i in range(len(infile.pages)):
    p = infile.pages[i]
    if i == 20:
        output.add_page(p2)
    else:
        output.add_page(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)
