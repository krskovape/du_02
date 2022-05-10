Zde je popsáno, jak program GTFS a nejfrekventovanější mezizastávkový úsek funguje a jak je strukturován.
### Sturktura

V souboru `get_data.py` je definována funkce, která je následně volána v souboru `litacka.py` a je použita pro stažení a rozbalení dat. 
K otevírání dat slouží třída `GTFSTable`, od které následně dědí zbylé třídy. 
Samotným datům jsou s pomocí odpovídajících tříd inicializovány objekty. 

Třídy `Stop`, `StopTime`, `Trip`, a `Route` obsahují funkci `__init__()` a `elements_from_file()`, která volá načítací funkci a následně vytváří jednotlivé objekty. Funkce vrací seznamy objektů a třídy jsou vzájemně propojeny pomocí slovníků. 

Třída `StopSegment` je tvořena funkcemi `__init__()` a `create_segments()`, kde dochází k samotnému vytváření mezizastávkových segmentů. Výsledky jsou vraceny formou slovníku. 

Slovník s úseky je následně setřízen funkcí `sorted()` podle počtu spojů.

### Výsledky
Do konzole je vypsáno pět nejfrekventovanějších mezizastávkových úseků s názvem počáteční a koncové zastávky, počtem spojů a názvy linek. 