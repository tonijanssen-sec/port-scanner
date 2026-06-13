import socket
import argparse
portliste = (22, 23, 25, 53, 67, 68, 80, 110, 123, 143, 443, 445 ) #ein tuple, unveränderbar im Prozess

def main():
    parser = argparse.ArgumentParser(description="Einfacher TCP-Port-Scanner. Prüft eine oder mehrere Ziel-IPs auf offene Ports. by tonijanssen-sec") #parser erstellen
    parser.add_argument('ziele', type=str, nargs='+', help="Eine oder mehrere Ziel-IPs. Mehrere durch Leerzeichen trennen (kein Komma).") # Pflichtangabe: mindestens eine Ziel-IP (String), mehrere möglich = nargs'+'
    parser.add_argument('--ports', type=int, nargs='*', default=portliste, help="Zu scannende Ports, durch Leerzeichen getrennt (kein Komma). Ohne Angabe: Standard Portliste.") #parser Argument erstellen, ports sind optional sonst default Wert
    parser.add_argument('--timeout', type=float, default=1.0, help="Timeout pro Port in Sekunden (Standard 1.0). LAN: 0.1-0.2; über VPN höher.") #default timeout ist auf 1.0 gesetzt, kann im LAN auch auf 0.2 gesetzt werden
    args = parser.parse_args() # parsed die Argumente
    
    for ziel in args.ziele: # zieht sich die Ziele aus der Eingabe des Benutzers
        for port in args.ports: # zieht die Zielports aus der Eingabe des Benutzers
            fStringOffen = f"Ziel-IP: {ziel} mit der Portnummer {port} ist offen." #fString = formattierter String
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Modul socket → Funktion socket(), AF_INET = IPv4, SOCK_STREAM = TCP
            s.settimeout(args.timeout) #socket timeout nach 1.0 sek
            ergebnis = s.connect_ex((ziel, port)) # 0 = offen, sonst Fehlercode (errno) = zu/gefilter
            if ergebnis == 0: # also wenn ergebnis offen ist, printe es
                print(fStringOffen)
            s.close() # schließt alle Sockets, WICHTIG, bei sehr vielen sprich 65.535 Ports scans kann System sonst abschmieren! 

if __name__ == "__main__": #prüft: wird das skript direkt aufgerufen? Wenn ja rufe main() funktion auf
    main()
