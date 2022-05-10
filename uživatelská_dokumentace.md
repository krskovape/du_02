# GTFS a nejfrekventovanější mezizastávkový úsek

Program `GTFS a nejfrekventovanější mezizastávkový úsek` načítá jízdní řády z formátu GTFS a následně určuje nejfrekventovanější mezizastávkový úsek. Výsledky jsou seřazeny podle počtu spojů a vypsány do konzole. 

### Automatické stažení dat
Při spuštění program pomocí `get_data.py` funkcí `retrieve_data` automaticky stáhne a rozzipuje potřebná data. Ta jsou uložena do nově vytvořené složky s názvem `gtfs`, kdy s nimi dále pracuje program `lítačka.py`.

### Třídy
**GFSTable**
Třída slouží pro definování funkce stahující data. Následující třídy dědí.  

Ve třídách `Stop`, `StopTime`, `Trip`, a `Route` dojde k inicializaci jednotlivých objektů z dat.

**StopSegment**
V této třídě dochází k vytvoření jednotlivých mezizastávkových úseků.

### Výsledky
Program do konzole vypíše pět nejfrekventovanějších mezizastávkových úseků, název počáteční a koncové zastávky, počet spojů a rovněž názvy linek. 