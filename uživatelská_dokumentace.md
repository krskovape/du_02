# GTFS a nejfrekventovanější mezizastávkový úsek

Program `GTFS a nejfrekventovanější mezizastávkový úsek` načítá jízdní řády z formátu GTFS a následně určuje nejfrekventovanější mezizastávkový úsek. Výsledky jsou seřazeny podle počtu spojů a vypsány do konzole. 

### Automatické stažení dat
Při spuštění se program zeptá uživatele, zda si přeje stáhnout data. Pokud je odpověď *ano*, program z `get_data.py` funkcí `retrieve_data` je automaticky stáhne a rozbalí do nově vytvořené složky s názvem `gtfs`. Data jsou stahována z portálu Pražské integrované dopravy. Jestliže uživatel zvolí *ne* jako odpověď a má již existující složku `gtfs` s příslušnými daty, program proběhne na nich. Pokud je složka prázdná či neexistuje, program neproběhne. Při zadání jakéhokoliv jiného vstupu bude uživatel vyzván, aby znovu zadal správnou odpověď, tedy *ano* či *ne*. 

### Výsledky
Program do konzole vypíše pět nejfrekventovanějších mezizastávkových úseků, název počáteční a koncové zastávky, počet spojů a rovněž názvy linek. 
