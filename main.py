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
    if arg == "per_fifo":
        periodic_fifo()
    if arg == "per_lifo":
        periodic_lifo()

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
    #processing
    end = 0 #Endbestand
    for a in list:
        end = end + float(a[0])
    print("Endbestand: " + str(end))

    #last index is still in the depot when the rest gets picked first, which means the last prize has to be taken.
    min = len(list)-1
    bew_end = 0
    while end > 0:
        min = find_lifo(list,min)
        if float(list[min][0]) > end:
            bew_end = bew_end + end * float(list[min][1])
            end = end - end
        else:
            bew_end = bew_end + abs(float(list[min][0]))*float(list[min][1])
            end = end - abs(float(list[min][0]))
        min -= 1

    bew_mat = 0
    outs = 0
    for a in list:
        if float(a[0])>0:
            bew_mat = bew_mat + float(a[0])*float(a[1])
        else:
            outs = outs + abs(float(a[0]))

    mat_cost = bew_mat - bew_end
    av_cost = mat_cost/outs
    print(list)
    print("bewerteter Endbestand: {}\nbewertete Zugänge: {}\nKosten durch Abgänge: {} \ndurchschnittliche Kosten: {:.2f} euro/unit".format(bew_end,bew_mat,mat_cost,av_cost))

def periodic_lifo():
    pass

def permanent_fifo():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)

    #processing
    i = 1
    used_material = 0
    while i < len(list):
        #Wenn Abgang
        if float(list[i][0])<0:
            while float(list[i][0])<0:
                spot = find_fifo(list)
                if spot==None:
                    break
                if float(list[spot][0])<abs(float(list[i][0])):
                    used_material = used_material + abs(float(list[spot][0])) * float(list[spot][1])
                    list[i][0] = str(float(list[spot][0])+float(list[i][0]))
                    list[spot][0] = "0"
                else:
                    used_material = used_material + abs(float(list[i][0])) * float(list[spot][1])
                    list[spot][0]=str(float(list[spot][0])+float(list[i][0]))
                    list[i][0]="0"
            #Wenn Schritte erwünscht: Hier auskommentieren
            #print(list)
        i += 1
    print(list)
    print("bewerteter Endbestand: {}\nbewerteter Materialverbrauch: {}".format(calculate(list), used_material))

def permanent_lifo():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)

    #processing
    i = 1
    used_material = 0
    while i < len(list):
        #Wenn Abgang
        if float(list[i][0])<0:
            while float(list[i][0])<0:
                spot = find_lifo(list, i)
                if spot==None:
                    break
                if float(list[spot][0])<abs(float(list[i][0])):
                    used_material = used_material + abs(float(list[spot][0])) * float(list[spot][1])
                    list[i][0] = str(float(list[spot][0])+float(list[i][0]))
                    list[spot][0] = "0"
                else:
                    used_material = used_material + abs(float(list[i][0])) * float(list[spot][1])
                    list[spot][0]=str(float(list[spot][0])+float(list[i][0]))
                    list[i][0]="0"
            #Wenn Schritte erwünscht: Hier auskommentieren
            #print(list)
        i += 1
    #process amount of used material
    print(list)
    print("bewerteter Endbestand: {}\nbewerteter Materialverbrauch: {}".format(calculate(list),used_material))
    #print(calculate(list))

def find_fifo(list):
    i = 0
    for a in list:
        if float(a[0]) > 0:
            return i
        i+=1

def find_lifo(list, min):
    i = min
    #list = reversed(list)
    while i>=0:
        if float(list[i][0]) > 0:
            return i
        i-=1

def calculate(list):
    result = 0
    for a in list:
        if float(a[0])>0:
            result = result + float(a[0])*float(a[1])
    return result

periodic_fifo()
if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print("no arguments found - select a procedure") #add -h
    pass






