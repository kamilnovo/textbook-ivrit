#!/usr/bin/env python3
import sys

def view_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
            if not lines: return
            
            header = lines[0].lstrip('#').split(';')
            # Hlavička s jasným oddělením
            print(f"\033[1m{'ID':<5} | {'SLOVÍČKO':<20} | {'KOŘEN':<10} | {'VÝSLOVNOST':<15} | {'VÝZNAM'}\033[0m")
            print("-" * 80)
            
            for i, line in enumerate(lines[1:], 1):
                clean_line = line.lstrip('\u200e')
                parts = clean_line.split(';')
                if len(parts) < 4: continue
                
                # Prefix [i] zajistí LTR zobrazení celého řádku
                print(f"[{i:02}] {parts[0]:<20} | {parts[1]:<10} | {parts[2]:<15} | {parts[3]}")
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        view_csv(sys.argv[1])
    else:
        print("Použití: ./view_anki.py <soubor.csv>")
