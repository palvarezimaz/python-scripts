from PyPDF2 import PdfReader, PdfWriter
import sys

inputs = sys.argv[1:-1]
output_name = sys.argv[-1:]

def pdf_merger(pdf_list, output_name):
  merger = PdfWriter()
  for pdf in pdf_list:
    merger.append(pdf)

  output = open(f"{output_name[0]}", "wb")
  merger.write(output)
  merger.close()
  output.close()


pdf_merger(inputs, output_name)
