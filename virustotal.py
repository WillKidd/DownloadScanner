import time
from virustotal3.core import Files

def uploadFile(path_to_file):
    api_key = ""
    try:
        with open("config.txt", "r") as f:
            api_key = str(f.readlines()[0])
        fs= Files(api_key)
        result = fs.upload(path_to_file)
        print(fs.info_file(result["data"]["id"]))
    except Exception as e:
        print(e)
    finally:
        pass
