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
