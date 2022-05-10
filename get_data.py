# skript na automaticke stazeni a rozbaleni dat GTFS
from urllib.error import HTTPError
import requests, zipfile, io

from urllib3 import Timeout

def retrieve_data():
    try:
        print("Stahuju data.")
        r = requests.get("http://data.pid.cz/PID_GTFS.zip")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("gtfs")
        print("Hotovo.")

    except FileNotFoundError:
        print("Nelze otevřít soubor. Vybraný soubor buď neexistuje nebo je k němu zadána nekorektní cesta.")
        quit()
    except PermissionError:
        print("Program nemá povolení k přístupu k souboru.")
        quit() 
    except zipfile.BadZipFile:
        print("Soubor není .zip soubor.")
        quit()
    except zipfile.LargeZipFile:
        print("Soubor je pro program příliš velký na to, aby ho odzipoval.")
        quit()
    except ConnectionError:
        print("Chybí připojení k internetu.")
        quit()
    except HTTPError:
        print("Neúspěšný pokus o stažení dat.")
        quit()
    except TimeoutError:
        print("Vypršel čas požadavku.")
        quit()