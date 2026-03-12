#!/usr/bin/env python3
import sys

LRO = '\u202d'
PDF = '\u202c'

def view_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
            if not lines: return
            
            # Hlavička
            h_str = f"{'ID':<5} | {'SLOVÍČKO':<20} | {'KOŘEN':<10} | {'VÝSLOVNOST':<15} | {'VÝZNAM'}"
            print(f"{LRO}{h_str}{PDF}")
            print("-" * 80)
            
            for i, line in enumerate(lines[1:], 1):
                parts = line.split(';')
                if len(parts) < 4: continue
                
                # Každá buňka je LTR ostrov
                col1 = f"{LRO}{parts[0]:<20}{PDF}"
                col2 = f"{LRO}{parts[1]:<10}{PDF}"
                col3 = f"{parts[2]:<15}"
                col4 = parts[3]
                
                print(f"[{i:02}] {col1} | {col2} | {col3} | {col4}")
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        view_csv(sys.argv[1])
    else:
        print("Použití: ./view_anki.py <soubor.csv>")
