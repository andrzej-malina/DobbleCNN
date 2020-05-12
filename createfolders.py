import os

#current folder directory
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
#list of all labels that occur in the cards
labels = ['ok', 'kropla', 'kaktus', 'ksiezyc', 'plama', 'stop', 'klodka', 'cel', 'kotwica', 'serce', 'bomba', 'zebra',
         'kostka_lodu', 'piesek', 'butelka', 'ser', 'konik', 'pajeczyna', 'marchewka', 'zegar', 'lisc', 'usta', 'jablko',
         'okulary', 'oko', 'gwiazdka', 'dinozaur', 'auto', 'zarowka', 'sniezynka', 'yingyang', 'wykrzyknik', 'ognisko',
         'ludek', 'stokrotka', 'klucz', 'klucz_muzyczny', 'doble', 'piorun', 'biedronka', 'duch', 'delfin', 'art',
         'czacha', 'olowek', 'pajak', 'smok', 'swieca', 'kotek', 'drzewo', 'balwan', 'pytajnik', 'balon', 'iglo',
         'koniczyna', 'klaun', 'nozyce' ]

#loop for creating new folder directories
for label in labels:
    os.mkdir(os.path.join(current_path, str(label)))
