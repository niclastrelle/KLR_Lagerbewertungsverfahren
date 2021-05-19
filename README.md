# KLR_Lagerbewertungsverfahren

Dieses Programm ermöglicht die automatische Bewertung von Lagerbeständen mittels standardisierter Verfahren.
Im Spezifischen sind schon integriert:
1. permanent FiFo
2. permanent LiFo
3. periodisch FiFo
4. periodisch LiFo
6. HiFo
7. LoFi


## Schrittanleitung zur Nutzung

1. Erstelle eine .csv Datei in dem folgenden Format: 

Quantität, Preis

Falls es nur einen Abgang gibt, dann wird der Preis weggelassen und ein negatives Vorzeichen vor dem Wert angegeben.
Es gibt eine Beispieldatei. Daran kann sich orientiert werden.

Die .csv Datei im selben Verzeichnis, wie main.py ablegen.

Zur Ausführung in die Konsole eingeben:

```
python main.py <Bewertungsmethode>
```

## Interpretation der Ergebnisse
Das Ergebnis ist eine Liste, welche die aktuellen Bestände darstellt. Bei Bedarf kann ein weiterer print-Befehl auskommentiert werden, um die Zwischenschritte auch auszugeben.
Diese Stelle ist markiert.

Der zweite Wert ist der Gesamtwert des Lagers. 
