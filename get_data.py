# skript na automaticke stazeni a rozbaleni dat GTFS
import requests, zipfile, io

def retrieve_data():
    try:
        print("Downloading data.")
        r = requests.get("http://data.pid.cz/PID_GTFS.zip")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("gtfs")
        print("Done.")

    except FileNotFoundError:
        print("Cannot open file. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print("Program doesn't have permisson to access file.")
        quit() 
    except zipfile.BadZipFile:
        print("File is not a ZIP file.")
        quit()
    except zipfile.LargeZipFile:
        print("File is too big for this program to unzipp it.")
        quit()
