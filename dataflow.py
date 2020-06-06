import os
from os import listdir, makedirs
from os.path import isdir, isfile, join

def show_files_in_folder(folder):
    return [f for f in listdir(folder) if isfile(join(folder, f))]

def create_prediction_folders(number):
    folder = 'test/predict{0}'.format(nr)
    if not isdir(folder):
        makedirs(folder)
        makedirs('{0}/predict'.format(folder))
    return folder

def get_labels():
    names = sorted(['ok', 'kropla', 'kaktus', 'ksiezyc', 'plama', 'stop', 'klodka', 'cel', 'kotwica', 'serce', 'bomba',
              'zebra', 'kostka_lodu', 'piesek', 'butelka', 'ser', 'konik', 'pajeczyna', 'marchewka', 'zegar', 'lisc', 'usta',
              'jablko','okulary', 'oko', 'gwiazdka', 'dinozaur', 'auto', 'zarowka', 'sniezynka', 'yingyang', 'wykrzyknik',
              'ognisko', 'ludek', 'stokrotka', 'klucz', 'klucz_muzyczny', 'doble', 'piorun', 'biedronka', 'duch', 'delfin', 'art',
              'czacha', 'olowek', 'pajak', 'smok', 'swieca', 'kotek', 'drzewo', 'balwan', 'pytajnik', 'balon', 'iglo',
              'koniczyna', 'klaun', 'nozyce'])

    labels = dict()

    for i in range(len(names)):
        labels[i] = names[i]

    return labels

def indices_to_labels(predicted_class_indices):
    labels = get_labels()
    return [labels[k] for k in predicted_class_indices]