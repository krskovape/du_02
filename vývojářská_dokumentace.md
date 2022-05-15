Zde je popsáno, jak program GTFS a nejfrekventovanější mezizastávkový úsek funguje a jak je strukturován.
## Sturktura

V souboru `get_data.py` je definována funkce, která je následně volána v souboru `litacka.py` a je použita pro stažení a rozbalení dat. 

#### Třída GTFSTable
Třída obsahuje metodu  `__init__` a třídní metodu `load_file`, která má jako parameter `file_name`, což je název `txt` souboru obsahující vstupní data. V nich jeden řádek odpovídá jednomu objektu a hodnoty jednotlivých atributů jsou od sebe odděleny čárkou. Metoda načte vstupní soubor pomocí `DictReader`. Jeho prvky jsou pak postupně procházeny `for` cyklem a přiřazovány do vytvořeného seznamu. Metoda pak vrací tento seznam.

#### Třída Stop
Tato třída dědí od třídy `GTFSTable` a obsahuje metodu `__init__` se vstupním parametrem `data`, který odpovídá slovníku obsahujícím data o jednom objektu.

Metoda třídy `elements_from_file` bere jako vstupní parametr `file_name`, což je opět název vstupního souboru, který je předáván metodě `load_file`. Metoda vrací seznam vytvořených objektů typu `Stop` (`list_stops`) a slovník (`dict_stops`), ve kterém jsou klíče tvořeny hodnotami `stop_id` a k nim jsou přiřazeny odpovídající `Stop` objekty.

#### Třída StopTime
Tato třída dědí od třídy `GTFSTable` a obsahuje metodu `__init__` se vstupním parametrem `data`, který odpovídá slovníku obsahujícím data o jednom objektu. Jako parametr `dict_trips` bere slovník, ve kterém jsou klíče tvořeny hodnotami atributu `trip_id` a k nim jsou přiřazeny odpovídající objekty typu `Trip`. Vstupní parametr `dict_stops` je slovník, jehož klíče jsou tvořeny hodnotami atributu `stop_id` a k nim jsou přiřazeny odpovídající `Stop` objekty.

Metoda třídy `elements_from_file` bere jako vstupní parametr `file_name`, což je název vstupního souboru (viz Třída GTFSTable). Dalšími vstupními parametry jsou slovníky `dict_trips` a `dict_stops` popsané u předchozí metody. Metoda pak vrací seznam (`list_stop_times`) obsahující všechny vytvořené objekty typu `StopTime`.

#### Třída Trip
Tato třída dědí od třídy `GTFSTable` a obsahuje metodu `__init__` se vstupním parametrem `data`, který odpovídá slovníku obsahujícím data o jednom objektu. Jako parametr `dict_routes` bere slovník, ve kterém jsou klíče tvořeny hodnotami atributu `route_id` a k nim jsou přiřazeny odpovídající objekty typu `Route`.

Metoda třídy `elements_from_file` bere jako vstupní parametr `file_name`, což je název vstupního souboru (viz Třída GTFSTable). Dalším vstupním parametrem je slovník `dict_routes` popsaný u předchozí metody. Metoda vrací seznam (`list_trips`) obsahující všechny vytvořené objekty typu `Trip` a slovník `dict_trips`, který obsahuje jako klíče hodnoty atributu `trip_id` a k nim přiřazené odpovídající objekty typu `Trip`.

#### Třída Route
Tato třída dědí od třídy `GTFSTable` a obsahuje metodu `__init__` se vstupním parametrem `data`, který odpovídá slovníku obsahujícím data o jednom objektu.

Metoda třídy `elements_from_file` bere jako vstupní parametr `file_name`, což je opět název vstupního souboru, který je předáván metodě `load_file`. Metoda vrací seznam vytvořených objektů typu `Route` (`list_routes`) a slovník (`dict_routes`), ve kterém jsou klíče tvořeny hodnotami `route_id` a k nim jsou přiřazeny odpovídající `Route` objekty.

#### Třída StopSegment
Tato třída dědí od třídy `GTFSTable` a obsahuje metodu `__init__` se vstupními parametry:
* `from_stop` - počáteční zastávka úseku, objekt typu `Stop`
* `from_stop` - koncová zastávka úseku, objekt typu `Stop`
* `trip` - spoj projíždějící daným úsekem, objekt typu `Trip`
* `route_short_name` - název linky projíždějící daným úsekem, proměnná typu `str`

Metoda třídy `create_segments` bere jako vstupní parametr seznam objektů typu `StopTime` (`list_stop_times`). Na úvod je vytvořen slovník `dict_stop_segments`, do kterého budou ukládány všechny mezizastávkové úseky. Následně jsou pomocí `for` cyklu načítány vždy dva po sobě následující objekty `StopTime`. Pomocí podmínky je zkontrolováno, že načtené objekty spadají do stejného spoje a že druhý načtený objekt následuje po prvním. Po splnění této podmínky je porovnána dvojice id počáteční a koncové zastávky. Pokud ve slovníku existuje objekt s tímto klíčem, je do jeho atributu `trips` přiřazen načtený spoj (objekt typu `Trip`), hodnota atributu `number_of_trips` je zvýšena o jedna a pokud atribut `routes` neobsahuje název linky, je do ní přiřazen. Pokud ve slovníku není klíč s danými id, je doplněn a jako jeho hodnota vytvořen nový mezizastávkový úsek, tedy objekt typu `StopSegment`. Metoda vrací slovník (`dict_stop_segments`) obasující dvojici id zastávek na pozici klíče a k nim přiřazené odpovídající mezizastávkové segmenty.


Proměnným `stop_file`, `routes_file`, `trips_file` a `stop_times_file` jsou nadefinovány odpovídající názvy `txt` souborů. Na dané třídy je zavolána funkce `elements_from_file` a jsou vytvořeny odpovídající seznamy a slovníky.

Na třídu `StopSegment` je zavolána funkce `create_segments` a výsledek uložen do slovníku `dict_stop_segments`. Ten je následně sestupně setříděn funkcí `sorted` podle počtu spojů (`number_of_trips`). Výsledek třídění je uložen do seznamu `segments_sorted`.

## Výsledky
Do konzole je vypsáno pět nejfrekventovanějších mezizastávkových úseků s názvem počáteční a koncové zastávky, počtem spojů a názvy linek. 
