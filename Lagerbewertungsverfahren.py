import csv
import sys

#format of the csv file has to be: modification as double, cost per unit as double
#at first, always the beginning state
#no checks if outtake > intake

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
    if arg == "per_hifo":
        periodic_hifo()
    if arg == "perm_hifo": #not added
        permanent_hifo()
    if arg == "per_lofo":
        periodic_lofo()
    if arg == "perm_lofo": #not added
        permanent_lofo()
    if arg == "dm":
        durchschnittspreismethode()
    if arg == "gl_dm":
        gleitende_durchschnittspreismethode()


def test():
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    print(list)

def durchschnittspreismethode():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    #processing
    #sum all quantities and costs
    Menge = 0
    AK = 0
    Abgaenge = 0
    for a in list:
        if float(a[0])>0:
            Menge = Menge + float(a[0])
            AK = AK + float(a[0])*float(a[1])
        else:
            Abgaenge = Abgaenge + abs(float(a[0]))
    Bestand = Menge - Abgaenge
    Durchschnittspreis = AK / Menge
    Endbestand = Bestand * Durchschnittspreis
    print("Durchschnittskosten: {} \nAbgänge: {} \nAnschaffungskosten: {} \nEndbestand: {} ".format(Durchschnittspreis, Abgaenge, AK, Endbestand))
    pass

def gleitende_durchschnittspreismethode():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    Menge = 0
    AK = 0
    i = 0
    for a in list:
        if float(a[0]) > 0:
            Menge = Menge + float(a[0])
            AK = AK + float(a[0])*float(a[1])
        else:
            Durchschnittspreis = AK / Menge
            AK = AK - abs(float(a[0])) * Durchschnittspreis
            print(str(i) + ". Durchschnittspreis: " + str(Durchschnittspreis))
            Menge = Menge - abs(float(a[0]))
            i += 1
    Durchschnittspreis = AK / Menge
    print("Durchschnittskosten: {} \nEndbestand: {} ".format(Durchschnittspreis, AK))
    pass

def periodic_hifo():
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
    print("Endbestand: " + str(end) + " Einheiten")

    #always beginning with highest
    min = 0
    bew_end = 0
    while end > 0:
        min = find_hifo(list)
        if float(list[min][0]) > end:
            bew_end = bew_end + end * float(list[min][1])
            list[min][0] = float(list[min][0])-end
            end = end - end
        else:
            bew_end = bew_end + abs(float(list[min][0]))*float(list[min][1])
            end = end - abs(float(list[min][0]))
            list[min][0] = 0
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

def permanent_hifo():
    pass

def periodic_lofo():
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
    print("Endbestand: " + str(end) + " Einheiten")

    #always beginning with highest
    min = 0
    bew_end = 0
    while end > 0:
        min = find_lofo(list)
        if float(list[min][0]) > end:
            bew_end = bew_end + end * float(list[min][1])
            list[min][0] = float(list[min][0])-end
            end = end - end
        else:
            bew_end = bew_end + abs(float(list[min][0]))*float(list[min][1])
            end = end - abs(float(list[min][0]))
            list[min][0] = 0
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

def permanent_lofo():
    pass

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
    print("Endbestand: " + str(end) + "Einheiten")

    #last index is still in the depot when the rest gets picked first, which means the last prize has to be taken.
    min = len(list)-1
    bew_end = 0
    while end > 0:
        min = find_lifo(list,min)
        if float(list[min][0]) > end:
            bew_end = bew_end + end * float(list[min][1])
            end = end - end
            #list[min][0] = float(list[min][0]) - end
        else:
            bew_end = bew_end + abs(float(list[min][0]))*float(list[min][1])
            end = end - abs(float(list[min][0]))
            #list[min][0] = 0
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
    print("Endbestand: " + str(end) + " Einheiten")

    #last index is still in the depot when the rest gets picked first, which means the last prize has to be taken.
    min = 0
    bew_end = 0
    while end > 0:
        min = find_fifo(list, min)
        if float(list[min][0]) > end:
            bew_end = bew_end + end * float(list[min][1])
            end = end - end
            # list[min][0] = float(list[min][0]) - end
        else:
            bew_end = bew_end + abs(float(list[min][0]))*float(list[min][1])
            end = end - abs(float(list[min][0]))
            # list[min][0] = 0
        min += 1

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


def permanent_fifo():
    #preprocessing
    with open("people.csv","r") as file:
        reader = csv.reader(file)
        list = []
        for row in reader:
            list.append(row)
    print(list)
    #processing
    i = 1
    used_material = 0
    while i < len(list):
        #Wenn Abgang
        if float(list[i][0])<0:
            while float(list[i][0])<0:
                spot = find_fifo(list,0)
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

def find_lofo(list):
    check = []
    for a in list:
        if float(a[0]) > 0:
            check.append(float(a[1]))
        else:
            check.append(0)
    max_val = max(check)
    index = check.index(max_val)
    return index

def find_hifo(list):
    check = []
    for a in list:
        if float(a[0]) > 0:
            check.append(float(a[1]))
        else:
            check.append(max(check)+1)
    max_val = min(check)
    index = check.index(max_val)
    return index

def find_fifo(list,min):
    if min==None:
        i = 0
    i=min
    while i<len(list):
        if float(list[i][0]) > 0:
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

gleitende_durchschnittspreismethode()
if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print("no arguments found - select a procedure") #add -h
    pass