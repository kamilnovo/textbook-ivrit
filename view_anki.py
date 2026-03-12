#!/usr/bin/env python3
import sys

# LRO (Left-to-Right Override) znak
LRO = '\u202d'
PDF = '\u202c' # Pop Directional Formatting

def view_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
            if not lines: return
            
            header = lines[0].lstrip('#').split(';')
            # Hlavička
            h_str = f"{'ID':<5} | {'SLOVÍČKO':<20} | {'KOŘEN':<10} | {'VÝSLOVNOST':<15} | {'VÝZNAM'}"
            print(f"{LRO}\033[1m{h_str}\033[0m{PDF}")
            print("-" * 80)
            
            for i, line in enumerate(lines[1:], 1):
                parts = line.lstrip('\u200e').split(';')
                if len(parts) < 4: continue
                
                # Sestavení řádku s LRO na začátku
                row_str = f"[{i:02}] {parts[0]:<20} | {parts[1]:<10} | {parts[2]:<15} | {parts[3]}"
                print(f"{LRO}{row_str}{PDF}")
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        view_csv(sys.argv[1])
    else:
        print("Použití: ./view_anki.py <soubor.csv>")
