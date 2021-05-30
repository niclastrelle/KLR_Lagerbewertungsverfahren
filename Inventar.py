import csv
import sys

def build():
    with open("inventar.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    print(list)

build()