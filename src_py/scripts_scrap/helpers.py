import os
import time
import csv


def write_to_file(data, filename, path):
    with open(path + filename, "w") as text_file:
        text_file.write(data)
    text_file.close()


def open_file(filename, path):
    _file = open(path + filename,'r')
    return _file.read()


def timestamp():
    return str(time.strftime("%Y%m%d-%H%M%S"))


def determine_file_size(path, filename):
    statinfo = os.stat(path + filename)
    return statinfo.st_size


def read_from_dataset(file):
    movies = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        for entry in reader:
            movies.append(entry["title"])
    return movies


def compute_jaccard_index(title1, title2):
    # list_1 = list_1.replace("(","").replace(")","")
    # list_2 = list_2.replace("(","").replace(")","")
    set_1 = set(title1.split())
    set_2 = set(title2.split())
    return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))