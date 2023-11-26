"""
A quick script to open urls from a csv file. Run in WSL2 
"""
import sys
import csv
import subprocess
import time
import secrets



def link_opener(filename):
    en_profile, es_ope_profile = generate_random_profile()  
    file_lines_count, headers, en_url, es_url, ope_url = get_lines_content(filename)
    headers_string = ",".join(headers)
    print(f"Column headers are {headers_string}. There are {file_lines_count} URL lines")

    while (file_lines_count > 0):
        links_to_open_en = " ".join(en_url[:5])
        links_to_open_es_ope = " ".join(es_url[:5]) + " ".join(ope_url[:5])
        print(f"Opening {links_to_open_en}")
        print("&&")
        print(f"{links_to_open_es_ope}")

        open_chrome_tabs(en_profile, links_to_open_en)
        open_chrome_tabs(es_ope_profile, links_to_open_es_ope)

        file_lines_count = file_lines_count - 5
        en_url = en_url[5:]
        es_url = es_url[5:]
        ope_url = ope_url[5:]
        input("Press 'Enter' key for the next batch of URLs")
        close_chrome_tabs(en_profile, es_ope_profile)
        time.sleep(5)

    clean_up(en_profile, es_ope_profile)
    return


def open_chrome_tabs(profile, urls):
    subprocess.run(['powershell.exe', '-Command', f'Start-Process "chrome.exe" -ArgumentList "--user-data-dir={profile} {urls}"'])


def close_chrome_tabs(profile1, profile2):
    chrome_processes_1 = get_chrome_processes(profile1)
    subprocess.run(['powershell.exe', '-Command', f'Stop-Process -Id {str(chrome_processes_1[0])} -Force'])
    
    chrome_processes_2 = get_chrome_processes(profile2)
    subprocess.run(['powershell.exe', '-Command', f'Stop-Process -Id {str(chrome_processes_2[0])} -Force'])
  

def generate_random_profile():
    en_profile = f"C:\\deleteme\\{secrets.token_hex(8)}"
    es_ope_profile = f"C:\\deleteme\\{secrets.token_hex(8)}"
    return en_profile, es_ope_profile


def get_chrome_processes(profile):
    return subprocess.check_output(['powershell.exe', '-Command', f'Get-CimInstance Win32_Process | Where-Object {{$_.CommandLine -like "*{profile}*"}} | Select-Object -ExpandProperty ProcessId'], text=True).split()


def clean_up(profile1, profile2):
    subprocess.run(['powershell.exe', '-Command', f'Remove-Item -Path "{profile1}" -Recurse -Force'])
    subprocess.run(['powershell.exe', '-Command', f'Remove-Item -Path "{profile2}" -Recurse -Force'])


def get_lines_content(filename):
    with open(filename, "r", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader, None) 

        file_lines_count = 0
        en_url = []
        es_url = []
        ope_url= []

        for row in csv_reader:
            if row:
                file_lines_count += 1
                if len(row) >= 3:
                    en_url.append(row[0])
                    es_url.append(row[1])
                    ope_url.append(row[2])
                
    return file_lines_count, headers, en_url, es_url, ope_url


def main():
    if len(sys.argv) != 2:
        print("Error: Please provide which filename.csv you want to open")
        print("Use this script as:")
        print("$ python3 link-opener.py <filename>")
        sys.exit(1)    

    filename = sys.argv[1]
    checkFileType = filename.split(".")[1]
    if checkFileType != "csv":
        print("Error: Wrong filetype, please convert to .CSV")
        sys.exit(1)
    
    print(f"Opening urls from {filename}...")
    
    link_opener(filename)

    print("..done!")



if __name__ == '__main__':
    main()