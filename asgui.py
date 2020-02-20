adatok = []

def F1():
    fbe = open('naplo.txt', "r")
    for sor in fbe:
        if sor[0] == '#':
            eleje = sor.strip().split()
            eleje.pop(0)
        else:
            hianyzo = sor.strip().split()
            adat = eleje+hianyzo
            adatok.append(adat)
    print(adatok)

def F2():
    print('A 2. feladat')
    print('A naplóban' ,len(adatok), 'bejegyzés van')

def F3():
    jelen = 0
    hiányzik = 0
    for sor in adatok:
        for i in range(6):
            if sor[4][i] == 'I':
                jelen += 1
            if sor[4][i] == 'X':
                hiányzik += 1

    print(jelen)
    print(hiányzik)
            
            
F1()
F2()
F3()
