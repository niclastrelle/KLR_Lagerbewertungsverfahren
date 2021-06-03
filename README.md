# KLR_Lagerbewertungsverfahren

Dieses Programm ermöglicht die automatische Bewertung von Lagerbeständen mittels standardisierter Verfahren.
Im Spezifischen sind schon integriert:
1. permanent FiFo - "perm_fifo"
2. periodisch FiFo - "per_fifo"
3. permanent LiFo - "perm_lifo"
4. periodisch LiFo - "per_lifo"
5. periodisch HiFo - "per_hifo"
6. permanent HiFo - "perm_hifo"
7. periodisch LoFo - "per_lofo"
8. permanent LoFo - "perm_lofo"
9. periodische Durchschnittsmethode - "dm"
10. gleitende Durchschnittsmethode - "gl_dm"


### Schrittanleitung zur Nutzung

Erstelle eine .csv Datei in dem folgenden Format:   
Quantität, Preis

Diese muss im selben Verzeichnis, wie die Lagerbewertungsverfahren.py Datei platziert werden. Der Standard-Seperator ist ",". Es muss also für Kommazahlen ein "." verwendet werden.
Falls es einen Abgang gibt, dann wird der Preis weggelassen und ein negatives Vorzeichen vor dem Wert angegeben.
Es gibt eine Beispieldatei. Daran kann sich orientiert werden.

Zur Ausführung eines Lagerbewertungsverfahrens in die Konsole eingeben:

```
python Lagerbewertungsverfahren.py <Bewertungsmethode>
```

Ergebnisse werden in der Konsole ausgegeben
