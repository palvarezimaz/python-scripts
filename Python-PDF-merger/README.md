# Python PDF merger

This very small Python program uses the PyPDF2 library to merge PDF files using the CLI, so I can stop using dodgy plugins.

## How to use

On your CLI, run the program listing first the sources, and then the desired filename for the target:

`python3 main.py source1.pdf source2.pdf ... target.pdf`

Note: the program follows the arguments order in a FIFO pattern


## Installation
To make it work, you need to install [PyPDF2](
https://pypi.org/project/PyPDF2/):

`pip install PyPDF2`

And, of course, have Python3 installed.

I want to thank all those annonymous heroes that put code online, daily, as it was the internet who guided me to make this code and this short program a working one.