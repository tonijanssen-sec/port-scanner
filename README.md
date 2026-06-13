# Port Scanner

Ein Port Scanner geschrieben in Python. Sucht offene Ports auf IPv4 und gibt diese aus.

### Wieso und wozu? 

Eine Übung zum Thema Schleifen da in der Umschulung demnächst eine Klausur in Programmiertechnik ansteht.

Ich will mir mehr skills aneignen, eigene Tools und automatisierte Skripte entwickeln welche speziell zum Thema Cybersecurity / Offensive Security passen.

Dies dient auch der Vorbereitung auf mein Praktikum in der IT-Sicherheit.

```python
import socket
zielliste = ("<erste Ziel IP>", "<zweite Ziel IP>")
portliste = (22, 23, 25, 53, 67, 68, 80, 110, 123, 143, 443, 445 ) #ein tuple, unveränderbar im Prozess

for ziel in zielliste:
    for port in portliste:
        fStringOffen = f"Ziel-IP: {ziel} mit der Portnummer {port} ist offen." #fString = formattierter String
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5) #socket timeout nach 1.5 sek
        ergebnis = s.connect_ex((ziel, port)) # 0 = offen, sonst Fehlercode (errno) = zu/gefilter
        if ergebnis == 0:
            print(fStringOffen)
        s.close()
```

### Was ich mit diesem Projekt gelernt habe

- Variablen und Datentypen in python (str, int, float, bool)
- Tuple vs. List und wann man was nimmt
- if-Verzweigungen funktionieren auch ohne else
- for-Schleifen über Tuples (einzeln und verschachtelt)
- f-strings dienen zum formatieren der Ausgabe
- Sockets: 
    - erstellen eines Sockets
    - wie ich einen Timeout setze
    - wie ich diesen verbinde
    - wie ich einen Socket schließe
- dass `connect_ex` 0 bei Erfolg wiedergibt und sonst einen Fehlercode
- verschachtelte Schleifen (nested loops), mehrere Ziele × mehrere Ports
