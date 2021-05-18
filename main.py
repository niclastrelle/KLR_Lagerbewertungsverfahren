import csv
import sys

#format of the csv file has to be: modification as double, cost per unit as double
#at first, always the beginning state

def main(arg):
    if arg == "test":
        test()
    if arg == "perm_fifo":
        permanent_fifo()

def test():
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    print(list)

def permanent_fifo():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)

    #processing
    #aktuell = int(list[0][0])*int(list[0][1])
    i = 1
    while i < len(list):
        #Wenn Abgang
        if int(list[i][0])<0:
            while int(list[i][0])<0:
                spot = find(list)
                if int(list[spot][0])<int(list[i][0]):
                    list[spot][0] = "0"
                    list[i][0] = str(int(list[spot][0])+int(list[i][0]))
                else:
                    list[spot][0]=str(int(list[spot][0])+int(list[i][0]))
                    list[i][0]="0"


        i += 1
    print(list)

def find(list):
    i = 0
    for a in list:
        if int(a[0]) > 0:
            return i
        i+=1

permanent_fifo()
if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print("no arguments found - select a procedure") #add -h
    pass






