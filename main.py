import csv
import sys

#format of the csv file has to be: modification as double, cost per unit as double
#at first, always the beginning state

def main(arg):
    if arg == "test":
        test()
    if arg == "perm_lifo":
        permanent_lifo()

def test():
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    print(list)

def permanent_lifo():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)

    #processing
    aktuell = int(list[0][0])*int(list[0][1])
    i = 1
    print(len(list))
    while i <= len(list):
        #Wenn Abgang
        print(i)
        i += 1
    print("test")

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print("no arguments found - select a procedure") #add -h
    main(sys.argv[1])
    pass


