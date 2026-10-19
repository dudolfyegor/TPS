def salva_appunto(testo):
    with open("dati/appunti.txt", "a", encoding="utf-8") as f:
        f.write(testo + "\n")

salva_appunto("comprare il libro")
salva_appunto("ripassare i file")
salva_appunto("consegnare su GitHub")

with open("appunti.txt", "r", encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=1):
        print(numero, riga.strip())

#ES 2


def conta_righe(nome_file):
    totali = 0
    piene = 0
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            totali += 1
            if riga.strip() != "":
                piene += 1
    return totali, piene

for nome in ["dati/parole.txt", "dati/commedia.txt"]:
    tot, piene = conta_righe(nome)
    print(f"{nome}: {tot} righe, {piene} non vuote")

#ES 3 

def parola_piu_lunga(nome_file):
    migliore = ""
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            for parola in riga.split():
                pulita = parola.strip(".,;:!?«»'\"")
                if len(pulita) > len(migliore):
                    migliore = pulita
    return migliore

p = parola_piu_lunga("dati/commedia.txt")
print(p, "-", len(p), "lettere")


#ES 4

import csv

def prezzo_medio(nome_file, alimentazione):
    somma = 0
    quante = 0
    with open(nome_file, "r", encoding="utf-8", newline="") as f:
        for auto in csv.DictReader(f):
            if auto["Fuel type"] == alimentazione:
                somma += int(auto["Price"])
                quante += 1
    if quante == 0:
        return None
    return round(somma / quante, 2)

for tipo in ["Petrol", "Diesel", "Hybrid", "Elettrica"]:
    print(tipo, "->", prezzo_medio("dati/car_sales_data.csv", tipo))



#es 5 


def filtra(origine, destinazione, marca, anno_minimo):
    selezionate = []
    with open(origine, "r", encoding="utf-8", newline="") as f:
        for auto in csv.DictReader(f):
            if auto["Manufacturer"] == marca and int(auto["Year of manufacture"]) >= anno_minimo:
                selezionate.append([auto["Model"], auto["Year of manufacture"], auto["Price"]])

    selezionate.sort(key=lambda r: int(r[2]), reverse=True)

    with open(destinazione, "w", encoding="utf-8", newline="") as f:
        scrittore = csv.writer(f)
        scrittore.writerow(["Model", "Year", "Price"])
        scrittore.writerows(selezionate)

    return len(selezionate)

quante = filtra("dati/car_sales_data.csv", "porsche.csv", "Porsche", 2015)
print("auto salvate:", quante)

with open("porsche.csv", "r", encoding="utf-8") as f:
    for i, riga in enumerate(f):
        if i == 4:
            break
        print(riga.strip())
        

