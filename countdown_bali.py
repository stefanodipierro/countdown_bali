import datetime
import time
from zoneinfo import ZoneInfo  # da Python 3.9 in poi

def main():
    # Imposta l'anno di destinazione (per il prossimo capodanno)
    new_year = datetime.datetime(2025, 1, 1, 0, 0, 0, tzinfo=ZoneInfo("Asia/Makassar"))
    print("Script avviato...")
    
    while True:
        now_bali = datetime.datetime.now(ZoneInfo("Asia/Makassar"))
        delta = new_year - now_bali

        if delta.total_seconds() <= 0:
            print("Buon Anno a Bali!")
            break
        
        giorni = delta.days
        ore, resto = divmod(delta.seconds, 3600)
        minuti, secondi = divmod(resto, 60)
        
        print(f"Mancano {giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi al Capodanno di Bali.")
        time.sleep(1)

if __name__ == "__main__":
    main()
