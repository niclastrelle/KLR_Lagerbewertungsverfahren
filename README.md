# KLR_Lagerbewertungsverfahren

Dieses Programm ermöglicht die automatische Bewertung von Lagerbeständen mittels standardisierter Verfahren.
Im Spezifischen sind schon integriert:
1. permanent FiFo
2. permanent LiFo
3. periodisch FiFo
4. periodisch LiFo
5. HiFo
6. LoFo


## Schrittanleitung zur Nutzung

Erstelle eine .csv Datei in dem folgenden Format: 

Quantität, Preis

Diese muss im selben Verzeichnis, wie die main.py Datei. Der Standard-Seperator ist ",". Es muss also für Kommazahlen ein "." verwendet werden.
Falls es nur einen Abgang gibt, dann wird der Preis weggelassen und ein negatives Vorzeichen vor dem Wert angegeben.
Es gibt eine Beispieldatei. Daran kann sich orientiert werden.

Zur Ausführung in die Konsole eingeben:

```
python main.py <Bewertungsmethode>
```

## Hinweise zur Interpretation der Ergebnisse
Das Ergebnis ist eine Liste, welche die aktuellen Bestände darstellt. Bei Bedarf kann ein weiterer print-Befehl auskommentiert werden, um die Zwischenschritte auch auszugeben.
Diese Stelle ist markiert.

Ergebnisse werden in der Konsole ausgegeben
