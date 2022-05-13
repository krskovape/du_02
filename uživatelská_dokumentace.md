# GTFS a nejfrekventovanější mezizastávkový úsek

Program `GTFS a nejfrekventovanější mezizastávkový úsek` načítá jízdní řády z formátu GTFS a následně určuje nejfrekventovanější mezizastávkový úsek. Výsledky jsou seřazeny podle počtu spojů a vypsány do konzole. 

### Automatické stažení dat
Při spuštění program pomocí `get_data.py` funkcí `retrieve_data` automaticky stáhne a rozzipuje potřebná data. Ta jsou uložena do nově vytvořené složky s názvem `gtfs`, kdy s nimi dále pracuje program `lítačka.py`.

### Výsledky
Program do konzole vypíše pět nejfrekventovanějších mezizastávkových úseků, název počáteční a koncové zastávky, počet spojů a rovněž názvy linek. 