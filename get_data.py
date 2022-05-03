# skript na automaticke stazeni a rozbaleni dat GTFS
import requests, zipfile, io

def get_data(file_name):
    try:
        r = requests.get("http://data.pid.cz/PID_GTFS.zip")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("gtfs")
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to access file {file_name}.")
        quit() 
    except zipfile.BadZipFile:
        print(f"{file_name} file is not a ZIP file.")
        quit()
    except zipfile.LargeZipFile:
        print(f"{file_name} file is too big for this program to unzipp it.")
        quit()