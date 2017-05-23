Eine Deutschland-Karte der Funkamateure basierend auf der Rufzeichenliste der Bundesnetzagentur

von Ulrich Thiel, VK2UTL/DK1UT

---

Mit Hilfe einiger Python-Skripte habe ich die Daten der (öffentlichen) [Rufzeichenliste der Bundesnetzagentur](https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/Rufzeichenliste/Rufzeichenliste_AFU.html) in eine SQL-Datenbank extrahiert und die Adressen mit Hilfe von GoogleMaps visualisiert. Das Resultat ist unten und **[hier](https://fusiontables.googleusercontent.com/embedviz?q=select+col8+from+1lGAOwlSUK7nCUsA0FlRRG9buB1QV51zNzJFUr7yj&viz=MAP&h=false&lat=51.2482144526009&lng=10.020759216308534&t=1&z=6&l=col8&y=2&tmplt=2&hml=TWO_COL_LAT_LNG)** im Vollbild zu sehen. Die Makierungen sind in zwei Farben nach Lizenzklasse aufgeteilt: rot für Klasse A und violett für Klasse E. Ich beschreibe unten kurz, wie ich vorgegangen bin, denn vielleicht kann das für andere Projekte auch nützlich sein.

<iframe width="500" height="600" scrolling="no" frameborder="no" src="https://fusiontables.google.com/embedviz?q=select+col8+from+1lGAOwlSUK7nCUsA0FlRRG9buB1QV51zNzJFUr7yj&amp;viz=MAP&amp;h=false&amp;lat=51.2482144526009&amp;lng=10.020759216308534&amp;t=1&amp;z=6&amp;l=col8&amp;y=2&amp;tmplt=2&amp;hml=TWO_COL_LAT_LNG"></iframe>

### Statistik

Stand: Mai 2017.

|   | Total  | Class A  | Class E |
|---|---|---|---|
| Records  |  76143 | 67975  |  8168 |
Distinct call signs|		 72322|64224|8098 |
Records w/ address|		 71338|64621|6717|
Distinct call signs w/ address|	 67517|60870|6647|
Records w/ geocode|		 70823|64141|6682|
Distinct call signs w/ geocode|	 67159|60545|6614| 

### Vorgehen

Bei der Rufzeichenliste der Bundesnetzagentur handelt es sich um eine PDF-Datei. Diese habe ich zunächst mit dem Linux-Tool ```ps2ascii``` in eine Text-Datei umgewandelt: 

```
ps2ascii Rufzeichenliste_AFU.pdf > calls.txt
``` 

Mit meinem Python-Skript ```makedb.py``` habe ich diese Text-Datei nun verarbeitet und aus den Daten eine SQL-Datenbank erstellt. Dies ist natürlich der schwierigste Teil. Erschwerend kommt hinzu, dass einige Rufzeichen mehrere Adressangaben haben und, dass Adressen teilweise schlicht fehlerhaft sind. Mein Skript sollte beide Fälle einigermaßen gut behandeln.   
Als nächstes habe ich mit meinem Skript ```makegeo.py``` geographische Koordinaten für die Adressen bestimmt (das nennt man *geocoding*). Für Python gibt es eine eigene Bibliothek namens geocoder, die direkten Zugriff auf die Google-API ermöglicht. Eine kleine Gemeinheit dabei ist, dass für private Zwecke nicht mehr als 2,5000 Abfragen pro Tag gemacht werden dürfen. Da die Datenbank mehr als 70,000 Einträge enthält, würde dies also einen Monat dauern. Glücklicherweise habe ich Zugriff auf einen Rechnerpool von dem ich diese Aufgabe aus in zwei Tagen erledigen konnte. Es sind schließlich ca. 500 Adressen übrig geblieben, für die ein Geocoding nicht erfolgreich war. Zum einen handelt es sich hierbei schlicht um Schreibfehler, die ich in dieser Menge nicht korrigieren wollte. Zum anderen scheinen es veraltete Adressen zu sein, die nicht mehr existieren.  
Nun habe ich mit meinem Python-Skript ```makecsv.py``` aus den Daten der SQL-Datenbank eine CSV-Datei erstellt. Diese Datei habe ich schließlich in eine [Google Fusion Table](usiontables.google.com) geladen, von wo aus sich die Daten sofort visualisieren lassen.

