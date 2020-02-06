import datetime

adat = []
def beolvas():
    fbe = open('lottosz.dat' , 'r')

    for elem in fbe.readlines():
        adat.append(list(map(int,elem.strip().split())))


def F1():
    
    z = sorted([int(x) for x in input('Mik voltak az e-heti lottószámok?').strip().split()][:5])
    adat.append(z)
    print(adat)

def F3():
    x = int(input('Adj meg egy egész számot:'))
    print(adat[x])
    
def F5():
    l = datetime.datetime.now()
    global számok
    számok = [0]*90
    for sor in adat:
        for elem in sor:
            számok[elem-1] +=1
    if számok.count(0)>0:
        print('VAN')
    else:
        print('NINCS')
    b = datetime.datetime.now()

def F6():
    x = 0
    for i in range(0, 90 , 2):
        x += számok[i]
    print(x)
    
        
    
    
beolvas()
F1()
F3()
F5()
F6()

