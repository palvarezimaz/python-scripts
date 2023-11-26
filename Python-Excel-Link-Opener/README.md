# Python+PowerShell CSV Url opener

Small script that grabs a .csv file and secuencially opens the urls into Chrome, automating the uber boring copy paste of urls to the browser. It is tailored to run on WSL2 but open Chrome on Windows (using PowerShell), and follows strict CSV especifications.

## How to use

On your CLI, run the program

`$ python3 link-opener.py <filename>`

The CSV file should have:
- 3 columns
- First line should be headers

Once it is run, it will open by 5 lines and it will wait for a terminal input to open the next 5 or remaining lines.

## Installation
Nothing special about this script, but it's always good idea to create a Virtual Environment

### VENV Creation
`$ python3 -m venv venv`

To activate
`$ source venv/bin/activate`

To deactivate
`$ deactivate`

## Special note
I want to thank all those annonymous heroes that put code online, daily, as it was the internet who guided me to make this code and this short program a working one.