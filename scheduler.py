import time
import os
import requests

cpt = 0

with open("/home/thisscpdoesnotexist/tsde/polling_api.key", "r") as f:
    NEXT_ROUND_KEY = f.read().rstrip()


while True:

    if cpt <=5:
        requests.get("http://thisscpdoesnotexist.pythonanywhere.com/save_data/?key=" + NEXT_ROUND_KEY)
        cpt +=1
    else:
        os.system('/home/thisscpdoesnotexist/tsde_scp_gen/generator.sh')
        cpt = 0




    time.sleep(3600)
    