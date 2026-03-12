#!/usr/bin/env python3
import csv
import sys

def view_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            if not lines: return
            
            # Zpracování hlavičky (odstranění # a rozdělení)
            header_line = lines[0].strip().lstrip('#')
            header = header_line.split(';')
            
            print(f"\033[1m{' | '.join([f'{h:<15}' for h in header[:4]])}\033[0m")
            print("-" * 70)
            
            for line in lines[1:]:
                # Odstranění LRM a rozdělení
                clean_line = line.strip().lstrip('\u200e')
                parts = clean_line.split(';')
                if len(parts) < 4: continue
                
                # Výpis prvních 4 sloupců se zarovnáním
                # Přidáváme LRM na konec hebrejských polí, aby terminál nepohltil mezeru
                print(f"{parts[0]:<15} | {parts[1]:<15} | {parts[2]:<15} | {parts[3]}")
    except FileNotFoundError:
        print(f"Soubor {filename} nebyl nalezen.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        view_csv(sys.argv[1])
    else:
        print("Použití: ./view_anki.py <soubor.csv>")
