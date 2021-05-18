import csv
import sys

#format of the csv file has to be: modification as double, cost per unit as double
#at first, always the beginning state

def main(arg):
    if arg == "test":
        test()
    if arg == "perm_fifo":
        permanent_fifo()
    if arg == "perm_lifo":
        permanent_lifo()

def test():
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    print(list)

def periodic_fifo():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)


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
        if float(list[i][0])<0:
            while float(list[i][0])<0:
                spot = find_fifo(list)
                if spot==None:
                    break
                if float(list[spot][0])<abs(float(list[i][0])):
                    list[i][0] = str(float(list[spot][0])+float(list[i][0]))
                    list[spot][0] = "0"
                else:
                    list[spot][0]=str(float(list[spot][0])+float(list[i][0]))
                    list[i][0]="0"
            #Wenn Schritte erwünscht: Hier auskommentieren
            #print(list)
        i += 1
    print(list)
    print(calculate(list))

def permanent_lifo():
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
        if float(list[i][0])<0:
            while float(list[i][0])<0:
                spot = find_lifo(list)
                if spot==None:
                    break
                if float(list[spot][0])<abs(float(list[i][0])):
                    list[i][0] = str(float(list[spot][0])+float(list[i][0]))
                    list[spot][0] = "0"
                else:
                    list[spot][0]=str(float(list[spot][0])+float(list[i][0]))
                    list[i][0]="0"
            #Wenn Schritte erwünscht: Hier auskommentieren
            #print(list)
        i += 1
    print(list)
    print(calculate(list))

def find_fifo(list):
    i = 0
    for a in list:
        if float(a[0]) > 0:
            return i
        i+=1

def find_lifo(list):
    i = len(list)-1
    for a in reversed(list):
        if float(a[0]) > 0:
            return i
        i-=1

def calculate(list):
    result = 0
    for a in list:
        if float(a[0])>0:
            result = result + float(a[0])*float(a[1])
    return result

permanent_lifo()
if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print("no arguments found - select a procedure") #add -h
    pass






