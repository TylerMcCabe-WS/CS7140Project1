import time
import os
import requests
import json

run_loop = True
file_number = 396643
file_prefix = 'KDE_JSON'
if not os.path.exists(file_prefix):
    try:
        os.mkdir(file_prefix)
    except Exception as e:
        print(e)
        raise
response_text = "https://bugs.kde.org/rest/bug?id="
i = 290290
gap = 1000
while i < 516516:
    if (not os.path.isfile(file_prefix+"/"+file_prefix+"_Bugs_"+str(i)+"-"+str(i+gap+1)+".json")):
        k=1
        response_copy = response_text+str(i)
        while k <= gap:
            response_copy = response_copy +"," +str(i+k)
            k+=1
        response_copy = response_copy +"," +str(i+k)
        response = requests.get(response_copy)
        if response.ok:
            data = response.json()
            print("Bugs "+str(i)+" through "+str(i+k)+" were downloaded.")
        else:
            print(f"Request failed with status code: {response.status_code}")
        filename = file_prefix+"_Bugs_"+str(i)+"-"+str(i+k)+".json"
        i+=k+1
        with open(os.path.join(file_prefix, filename), 'w') as f:
            json.dump(data, f, indent=4)
        time.sleep(1)
    else:
        i+=gap
        print("Bugs "+str(i)+"-"+str(i+gap+1)+ " already downloaded.")